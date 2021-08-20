# -*- coding: utf-8 -*-

{
    'name': 'Multi aprovador de ausencias mexico',
    'version': '14.1',
    'summary': """Multi aprovador de ausencias""",
    'description': 'Multi aprovador de ausencias, agrega tipos de ausencia con distintos aprovadores',
    'category': 'Generic Modules/Human Resources',
    'author': 'Luis Angel Alvarado Hernandez',
    'company': 'DatLag',
    'website': "https://dat-lag.com",
    'depends': ['base_setup', 'hr_holidays'],
    'data': [
        'views/leave_request.xml',
        'security/ir.model.access.csv',
        'security/security.xml'
    ],
    'demo': [],
    'images': ['static/description/banner.png'],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
    'application': True,
}
