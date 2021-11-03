{
    'name': 'Kinh Do Sale Management',
    'description': """
       Description of Kinh Do sale management module
    """,
    'author': 'Group xxx',
    'summary': 'Summany of sale management module',
    'version': '1.0.0',
    'category': 'Sales/Sales',
    'depends': ['sale'],
    'data':
        [
            'views/res_partner_views.xml',
            'views/sale_order_views.xml',
        ],
    'application': True,
    'installable': True,
}
