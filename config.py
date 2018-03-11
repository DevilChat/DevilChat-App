import os
basedir = os.path.abspath(os.path.dirname(__file__))

# The config file for now is set to mostly environment variables for development purposes.
class Config(object):
    # will need to change alternative key to a more secure option once out of development.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['inbox@paulgg.com']
    # Maybe we can replace the pagination feature with a refresh thing that Twitter does
    # when you continually scroll down.
    POSTS_PER_PAGE = 25
