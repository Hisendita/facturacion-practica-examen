# -*- coding: utf-8 -*-
{
    'name': "Examen3",

    'summary': """
        pending""",

    'description': """
        pending
    """,

    'author': "Sergi Lancero",
    'website': "http://www.sergilancero.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/clientes.xml',
        'views/detalle.xml',
        'views/facturas.xml',
        'views/productos.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True,
    'installable' : True,
}
