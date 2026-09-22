{
    'name': 'Super Clean — Website CRM',
    'version': '19.0.1.0.0',
    'summary': 'Adds French postcode field to Contact Us form and maps it to crm.lead.zip',
    'author': 'much. Consulting',
    'depends': ['website_crm'],
    'data': [
        'views/website_contactus_templates.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
