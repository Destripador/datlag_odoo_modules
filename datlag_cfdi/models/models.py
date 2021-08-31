# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from .fiel import Fiel
from .autenticacion import Autenticacion
from .solicitadescarga import SolicitaDescarga
from .verificasolicituddescarga import VerificaSolicitudDescarga
from .descargamasiva import DescargaMasiva
import base64
import os
import logging
import datetime
import time
_logger = logging.getLogger(__name__)

class inicio(models.Model):
     _name = 'datlag_cfdi.inicio'
     _description = 'modelo de pruba para subida de archivos'

     RFC = fields.Char(string="RFC")
     FIEL_CER = fields.Binary(string="cer")
     FIEL_KEY = fields.Binary(string="key")
     FIEL_PAS = fields.Char(string="contraseña")

     @api.model
     def validar(self, args):
         try:
             current_register = self.env['datlag_cfdi.inicio'].search([('id', '=', args['id'])], limit=1)
             fiel = Fiel(base64.decodebytes(current_register.FIEL_CER),base64.decodebytes(current_register.FIEL_KEY), current_register.FIEL_PAS)
             auth = Autenticacion(fiel)
             token = auth.obtener_token()
             return True
         except Exception as e:
             raise ValidationError("No se ha podido validar error 500.")

     @api.model
     def descargamasiva(self, args):
         _logger.error("IT IS Error: SOLICITUD::  " + str(args['start'].strptime('%Y ') ))
         args['start'], args['end']
         """current_register = self.env['datlag_cfdi.inicio'].search([('id', '=', args['id'])], limit=1)
         fiel = Fiel(base64.decodebytes(current_register.FIEL_CER),base64.decodebytes(current_register.FIEL_KEY), current_register.FIEL_PAS)
         auth = Autenticacion(fiel)
         token = auth.obtener_token()
         descarga = SolicitaDescarga(fiel)
         solicitud = descarga.solicitar_descarga(
             token, current_register.RFC, args['start'], args['end'], rfc_receptor=current_register.RFC, tipo_solicitud='Metadata'
         )
         _logger.error("IT IS Error: SOLICITUD::  " + str(solicitud))
         while True:
             token = auth.obtener_token()
             print('TOKEN: ', token)
             verificacion = VerificaSolicitudDescarga(fiel)
             verificacion = verificacion.verificar_descarga(
                 token, current_register.RFC, solicitud['id_solicitud'])
             _logger.error("IT IS Error: SOLICITUD::  " + str(verificacion))
             estado_solicitud = int(verificacion['estado_solicitud'])
             # 1, Aceptada
             # 2, En proceso
             # 3, Terminada
             # 4, Error
             # 5, Rechazada
             # 6, Vencida
             if estado_solicitud <= 2:
                 # Si el estado de solicitud esta Aceptado o en proceso el programa espera
                 # 60 segundos y vuelve a tratar de verificar
                 time.sleep(60)
                 continue
             elif estado_solicitud >= 4:
                 _logger.error("IT IS Error: error general ")
                 break
             else:
                 # Si el estatus es 3 se trata de descargar los paquetes
                 for paquete in verificacion['paquetes']:
                     _logger.error("IT IS Error: PAQUETE: "+ str(paquete))
                     descarga = DescargaMasiva(fiel)
                     _logger.error("IT IS Error: DESCARGA: "+ str(descarga))
                     descarga = descarga.descargar_paquete(token, current_register.RFC, paquete)
                     _logger.error("IT IS Error: DESCARGA: 1111111111"+ str(descarga))
                     #return descarga
                     #with open('{}.zip'.format(paquete), 'wb') as fp:
                     #    return base64.b64decode(descarga['paquete_b64'])
                 break
                """

     def authentication(self):
         """
         for record in self:
            FECHA_INICIAL = datetime.date(2020, 1, 2)
            FECHA_FINAL = datetime.date(2020, 2, 3)
            fiel = Fiel(base64.decodebytes(record.FIEL_CER),base64.decodebytes(record.FIEL_KEY), record.FIEL_PAS)

            auth = Autenticacion(fiel)

            token = auth.obtener_token()

            _logger.error("IT IS Error: " + str(token))

            descarga = SolicitaDescarga(fiel)

            solicitud = descarga.solicitar_descarga(
                token, record.RFC, FECHA_INICIAL, FECHA_FINAL, rfc_receptor=record.RFC, tipo_solicitud='Metadata'
            )

            _logger.error("IT IS Error: SOLICITUD::  " + str(solicitud))

            while True:

                token = auth.obtener_token()

                print('TOKEN: ', token)

                verificacion = VerificaSolicitudDescarga(fiel)

                verificacion = verificacion.verificar_descarga(
                    token, record.RFC, solicitud['id_solicitud'])

                _logger.error("IT IS Error: SOLICITUD::  " + str(verificacion))

                estado_solicitud = int(verificacion['estado_solicitud'])

                # 1, Aceptada
                # 2, En proceso
                # 3, Terminada
                # 4, Error
                # 5, Rechazada
                # 6, Vencida

                if estado_solicitud <= 2:

                    # Si el estado de solicitud esta Aceptado o en proceso el programa espera
                    # 60 segundos y vuelve a tratar de verificar
                    time.sleep(60)

                    continue

                elif estado_solicitud >= 4:

                    _logger.error("IT IS Error: error general ")

                    break

                else:
                    # Si el estatus es 3 se trata de descargar los paquetes

                    for paquete in verificacion['paquetes']:

                        _logger.error("IT IS Error: PAQUETE: "+ str(paquete))
                        descarga = DescargaMasiva(fiel)

                        _logger.error("IT IS Error: DESCARGA: "+ str(descarga))

                        descarga = descarga.descargar_paquete(token, record.RFC, paquete)

                        _logger.error("IT IS Error: DESCARGA: 1111111111"+ str(descarga))


                        #return descarga

                        #with open('{}.zip'.format(paquete), 'wb') as fp:

                        #    return base64.b64decode(descarga['paquete_b64'])

                    break
                    """
