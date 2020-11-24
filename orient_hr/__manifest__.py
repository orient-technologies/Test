# -*- coding: utf-8 -*-
{
    'name': "orient_hr",

    'summary': """
        Modified the homepage of HR module - employees module as per Orient's requirements
        """,

    'description': """
        Modified the homepage of HR module - employees module as per Orient's requirements
        while retaining the old pages accessible.
    """,

    'author': "Orient Technologies Pvt Ltd - Rishi Shetty",
    'website': "http://orientindia.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_attendance'],

    # always loaded
    'data': [
        'views/templates.xml',
        'security/ir.model.access.csv',
        'views/thoughts_master.xml',
    ],
    'demo':[
        'demo/demo.xml'
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
}
