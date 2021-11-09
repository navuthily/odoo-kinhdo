{
    'name': 'Kinh Do Sale Management',
    'description': """
       Description of Kinh Do sale management module
    """,
    'author': 'Na',
    'summary': 'Summany of sale management module',
    'version': '1.0.0',
    'category': 'Sales/Sales',
    'depends': ['sale','base','stock'],
    'data':
        [
            'views/res_partner_views.xml',
            'views/sale_order_views.xml',
            'views/stock_picking_views.xml'
        ],
    'application': True,
    'installable': True,
}
