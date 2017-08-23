def before_all(context):
    context.config.setup_logging()
    context.timeline=None
    context.client=None
