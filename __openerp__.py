# -*- coding: utf-8 -*-
{
    'name': "muti_base",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Auberon/MIS",
    'website': "http://www.mycompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'views/config_localization_view.xml',
        'data/xbase_data.xml',
        'data/res.company.csv',
        'data/config.area.csv',
        'data/config.branch.csv',
        'data/res.users.csv',
        'views/mutigroup_template.xml',
        'views/homepage_template.xml',
        'views/website_assets.xml',
    ],

}
