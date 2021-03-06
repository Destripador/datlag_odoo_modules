# -*- coding: utf-8 -*-
from odoo import models, api, fields, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class HrLeave(models.Model):
    _inherit = 'hr.leave'

    leave_approvals = fields.One2many('leave.validation.status',
                                      'holiday_status',
                                      string='Leave Validators',
                                      track_visibility='always',
                                      help="Leave approvals")
    multi_level_validation = fields.Boolean(
        string='Multiple Level Approval',
        related='holiday_status_id.multi_level_validation',
        help="If checked then multi-level approval is necessary")

    @api.model_create_multi
    def create(self, vals_list):
        holidays = super(HrLeave, self.with_context(mail_create_nosubscribe=True)).create(vals_list)
        for holiday in holidays:
            for values in vals_list:
                employee_id = values.get('leave_approvals', False)
                for x in employee_id:
                    current_employee = self.env['hr.employee'].search(
                                    [('user_id', '=', x[2]['validating_users'])], limit=1)

                    notifi=_('Hola ' + current_employee.name +', el empleado '+ holiday.employee_id.name +' del departamento '+ str(holiday.employee_id.department_id.name) +' tiene una peticion de ausencia pendiente para el dia '+ str(holiday.date_from.date()) +' Hasta '+str(holiday.date_to.date())+'<br><br>Revisa esta solicitud desde este boton <br><br><a href="/web#action=155" style="color:rgb(0, 12, 24);background-color:#fdb913;padding: 8px 16px 8px 16px; text-decoration: none; color: #fff; border-radius: 5px; font-size:13px;" data-original-title="" title="" aria-describedby="tooltip166299">Solicitudes pendientes</a>')

                    notification_ids = []
                    notification_ids.append((0,0,{
                        'res_partner_id': current_employee.user_id.partner_id.id,
                        'notification_type':'inbox'}))

                    holiday.employee_id.message_post(
                        body=notifi,
                        subject='Solicitud de vacaciones',
                        subtype_xmlid='mail.mt_comment',
                        email_layout_xmlid='mail.mail_notification_light',
                        author_id=self.env['res.users'].browse(1).id,
                        notification_ids=notification_ids,
                        message_type='notification',
                        partner_ids=[current_employee.user_id.partner_id.id]
                        )

        return holidays


        #_logger.error("IT IS Error: " + str(values.get('leave_approvals', False)))


    def action_approve(self):
        """ Compruebe si se agrega alguna tarea
        pendiente si as?? reasigna el pendiente tarea else llamar a la aprobaci??n  csacsacsa"""
        # if leave_validation_type == 'both':
        # this method is the first approval approval
        # if leave_validation_type != 'both': t
        # his method calls action_validate() below
        current_employee = self.env['hr.employee'].search(
            [('user_id', '=', self.env.uid)], limit=1)
        if any(holiday.state != 'confirm' for holiday in self):
            raise UserError(_(
                'Leave request must be confirmed ("To Approve")'
                ' in order to approve it.'))

        pro_vacation_project = self.sudo().env['ir.module.module'].search(
            [('name', '=', 'pro_vacation_project')],
            limit=1).state

        if pro_vacation_project == 'installed':
            return self.env['hr.leave'].check_pending_task(self)
        else:
            notifi=_('Hola ' + self.employee_id.name +', tu solicitud de ausencia del dia '+ str(self.date_from.date()) +' hasta '+ str(self.date_to.date()) +' ha sido revisada y aprovada por '+ current_employee.name +'. ')

            notification_ids = []
            notification_ids.append((0,0,{
                'res_partner_id': self.user_id.partner_id.id,
                'notification_type':'inbox'}))

            self.message_post(
                body=notifi,
                subtype_xmlid='mail.mt_comment',
                email_layout_xmlid='mail.mail_notification_light',
                author_id=self.env['res.users'].browse(1).id,
                message_type='notification',
                notification_ids=notification_ids
                )

            return self.approval_check()

    def approval_check(self):
        # Compruebe que todos los validadores de
        # licencia aprobaron la solicitud de licencia
        # si se aprueba Cambie la etapa de solicitud actual a Aprobado
        current_employee = self.env['hr.employee'].search(
            [('user_id', '=', self.env.uid)], limit=1)

        active_id = self.env.context.get('active_id') if self.env.context.get(
            'active_id') else self.id

        user = self.env['hr.leave'].search([('id', '=', active_id)], limit=1)
        for user_obj in user.leave_approvals.mapped(
                'validating_users').filtered(lambda l: l.id == self.env.uid):
            validation_obj = user.leave_approvals.search(
                [('holiday_status', '=', user.id),
                 ('validating_users', '=', self.env.uid)])
            validation_obj.validation_status = True
        approval_flag = True
        for user_obj in user.leave_approvals:
            if not user_obj.validation_status:
                approval_flag = False
        if approval_flag:
            user.filtered(
                lambda hol: hol.validation_type == 'both').sudo().write(
                {'state': 'validate1',
                 'first_approver_id': current_employee.id})
            user.filtered(
                lambda hol:
                not hol.validation_type == 'both').sudo().action_validate()
            if not user.env.context.get('leave_fast_create'):
                user.activity_update()
                #TODO: modificar plantilla de envio para que muestre una notificacion correcta
                notifi=_('Hola '+ user.employee_id.name +', tu ausencia pendiente para el dia '+ str(user.date_from.date()) +'&nbsp; hasta '+str(user.date_to.date())+' ha sido aprovada por todos los autorizadores.<br><br><p style="text-align: center;">No requiere de ninguna accion.</p>')

                notification_ids = []
                notification_ids.append((0,0,{
                    'res_partner_id': self.user_id.partner_id.id,
                    'notification_type':'inbox'}))

                self.message_post(
                    body=notifi,
                    subtype_xmlid='mail.mt_comment',
                    email_layout_xmlid='mail.mail_notification_light',
                        author_id=self.env['res.users'].browse(1).id,
                    message_type='notification',
                    notification_ids=notification_ids
                    )

            return True
        else:
            return False

    def action_refuse(self):
        """ Refuse the leave request if the current user is in
        validators list """

        current_employee = self.env['hr.employee'].search(
            [('user_id', '=', self.env.uid)], limit=1)

        approval_access = False
        for user in self.leave_approvals:
            if user.validating_users.id == self.env.uid:
                approval_access = True

        if approval_access:
            for holiday in self:

                if holiday.state not in ['confirm', 'validate', 'validate1']:
                    raise UserError(_(
                        'Leave request must be confirmed '
                        'or validated in order to refuse it.'))

                if holiday.state == 'validate1':
                    holiday.sudo().write(
                        {'state': 'refuse',
                         'first_approver_id': current_employee.id})
                else:
                    holiday.sudo().write(
                        {'state': 'refuse',
                         'second_approver_id': current_employee.id})
                # Delete the meeting
                if holiday.meeting_id:
                    holiday.meeting_id.unlink()
                # If a category that created several holidays,
                # cancel all related
                holiday.linked_request_ids.action_refuse()
            self._remove_resource_leave()
            self.activity_update()
            validation_obj = self.leave_approvals.search(
                [('holiday_status', '=', self.id),
                 ('validating_users', '=', self.env.uid)])
            validation_obj.validation_status = False

            notifi = _("Hola "+holiday.employee_id.name+", Tu ausencia del dia "+ str(holiday.date_from.date()) +" hasta "+ str(holiday.date_to.date()) +" ha sido denegada, esta decicion ha sido tomada por algun autorizador, si necesitas mas informacion puedes comunicarte con tu gerente u official de tiempos en el area de recursos humanos.")
            notification_ids = []
            notification_ids.append((0,0,{
            'res_partner_id':holiday.user_id.partner_id.id,
            'notification_type':'inbox'}))

            holiday.message_post(
                body=notifi,
                subtype_xmlid="mail.mt_comment",
                author_id=self.env['res.users'].browse(1).id,
                message_type='notification',
                notification_ids=notification_ids
                )
            return True
        else:
            for holiday in self:
                if holiday.state not in ['confirm', 'validate', 'validate1']:
                    raise UserError(_(
                        'Leave request must be confirmed '
                        'or validated in order to refuse it.'))

                if holiday.state == 'validate1':
                    holiday.write({'state': 'refuse',
                                   'first_approver_id': current_employee.id})
                else:
                    holiday.write({'state': 'refuse',
                                   'second_approver_id': current_employee.id})
                # Delete the meeting
                if holiday.meeting_id:
                    holiday.meeting_id.unlink()
                # If a category that created several holidays,
                # cancel all related
                holiday.linked_request_ids.action_refuse()
            self._remove_resource_leave()
            self.activity_update()
            return True

    def action_draft(self):
        """ Reset all validation status to false when leave request
        set to draft stage"""
        for user in self.leave_approvals:
            user.validation_status = False
        return super(HrLeave, self).action_draft()

    @api.onchange('holiday_status_id')
    def add_validators(self):
        """ Update the tree view and add new validators
        when leave type is changed in leave request form """
        li = []
        self.leave_approvals = [(5, 0, 0)]
        li2 = []
        for user in self.leave_approvals:
            li2.append(user.validating_users.id)
        for user in self.holiday_status_id.leave_validators.filtered(
                lambda l: l.holiday_validators.id not in li2):
            li.append((0, 0, {
                'validating_users': user.holiday_validators.id,
            }))
        self.leave_approvals = li

    def _get_approval_requests(self):
        """ Acci??n para el elemento del men?? Aprobaciones para mostrar la aprobaci??n
        solicitudes asignadas al usuario actual """

        current_uid = self.env.uid
        hr_holidays = self.env['hr.leave'].search([('state', '=', 'confirm')])
        li = []
        for req in hr_holidays:
            for user in req.leave_approvals.filtered(
                    lambda l: l.validating_users.id == current_uid):
                li.append(req.id)
        value = {
            'domain': str([('id', 'in', li)]),
            'view_mode': 'tree,form',
            'res_model': 'hr.leave',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'name': _('Approvals'),
            'res_id': self.id,
            'target': 'current',
            'create': False,
            'edit': False,
        }
        return value


class HrLeaveTypes(models.Model):
    """ Extender de modelo para agregar la aprobaci??n multinivel """
    _inherit = 'hr.leave.type'

    multi_level_validation = fields.Boolean(
        string='Multiple Level Approval',
        help="If checked then multi-level approval is necessary")
    leave_validation_type = fields.Selection(
        selection_add=[('multi', 'Multi Level Approval')])
    leave_validators = fields.One2many('hr.holidays.validators',
                                       'hr_holiday_status',
                                       string='Leave Validators',
                                       help="Leave validators")


    @api.onchange('leave_validation_type')
    def enable_multi_level_validation(self):
        """ Habilitaci??n del campo booleano de validaci??n multinivel"""
        self.multi_level_validation = True if (
                self.leave_validation_type == 'multi') else False


class HrLeaveValidators(models.Model):
    """ Model for leave validators in Leave Types configuration """
    _name = 'hr.holidays.validators'

    hr_holiday_status = fields.Many2one('hr.leave.type')

    holiday_validators = fields.Many2one('res.users',
                                         string='Leave Validators',
                                         help="Leave validators",
                                         domain="[('share','=',False)]")


class LeaveValidationStatus(models.Model):
    """ Modelo para validadores de licencia y su estado para cada solicitud de licencia """
    _name = 'leave.validation.status'

    holiday_status = fields.Many2one('hr.leave')

    validating_users = fields.Many2one('res.users', string='Leave Validators',
                                       help="Leave validators",
                                       domain="[('share','=',False)]")
    validation_status = fields.Boolean(string='Approve Status', readonly=True,
                                       default=False,
                                       track_visibility='always', help="Status")
    leave_comments = fields.Text(string='Comments', help="Comments")

    @api.onchange('validating_users')
    def prevent_change(self):
        """ Prevent Changing leave validators from leave request form """
        raise UserError(_(
            "Changing leave validators is not permitted. You can only change "
            "it from Leave Types Configuration"))
