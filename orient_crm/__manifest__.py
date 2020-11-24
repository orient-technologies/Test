# -*- coding: utf-8 -*-
{
    'name': "orient_crm",

    'summary': """
        Custom Dashboard added as homepage for CRM module""",

    'description': """
        Custom homepage added for CRM module while retaining
        the pipeline menuitem as it was and added a new menuitem for the new
        Homepage.
    """,

    'author': "Orient Technologies Pvt Ltd- Rishi Shetty",
    'website': "http://orientindia.com/",

    'category': 'Uncategorized',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead.xml',
    ],
    'installable': True,
    'application': True,
}
