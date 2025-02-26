from onlinequiz.wsgi import application  # Adjust this to your project’s name
from vercel_lambda_adapter import vercel_wsgi

handler = vercel_wsgi(application)
