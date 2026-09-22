def post_init_hook(env):
    env.cr.execute(
        "UPDATE ir_model_fields"
        " SET website_form_blacklisted = false"
        " WHERE model = 'crm.lead' AND name = 'zip'"
    )


def uninstall_hook(env):
    env.cr.execute(
        "UPDATE ir_model_fields"
        " SET website_form_blacklisted = true"
        " WHERE model = 'crm.lead' AND name = 'zip'"
    )
