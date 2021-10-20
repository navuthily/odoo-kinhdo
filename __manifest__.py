# -*- coding: utf-8 -*-
{
    'name': "Odoo kinh-do",
    'summary': """Odoo kinh-do""",
    'description': """Managing sale information""",
    'author': "na",
    'website': "https://odoo-kinhdo",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/quotation_views.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
