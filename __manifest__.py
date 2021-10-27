# -*- coding: utf-8 -*-
{
    'name': 'Kinhdo-sale',
    'version': '1.0',
    'author': '',
    'maintainer': '',
    'website': '',

    'description': """ """,
    'depends': ['base',"mail","product", "sale","purchase"],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        "views/client.xml",
        "views/product.xml",
        "views/product_type.xml",        
        

    ],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
