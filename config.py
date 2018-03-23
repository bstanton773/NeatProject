import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'only-brian-knows'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_DATABASE_URI = 'mysql://root:aaaaaa@localhost/test1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

