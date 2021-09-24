# -*- coding: utf-8 -*-
{
    'name': "Extra solicitudes",
    'summary': "Opciones extras para modulo de ausencias",
    'description': """
        El proposito de este modulo es agregar mas opciones a los tipos de ausencia.
    """,
    'author': "DatLag",
    'website': "https://datlag.com",
    'license': "AGPL-3",
    'images': ['static/description/banner.png'],
    'category': 'Generic Modules/Human Resources',
    'version': '0.1',
    'depends': ['base','hr_holidays'],
    'data': [
        'views/hr_leave_type.xml',
        'views/templates.xml',
    ],
    'application': True,
}
