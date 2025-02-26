from onlinequiz.wsgi import application  # Import your Django WSGI app

def handler(event, context):
    return application(event, context)
