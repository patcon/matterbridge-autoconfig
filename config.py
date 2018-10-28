import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    DEBUG = True
    SLACK_API_TOKEN = os.environ.get("SLACK_API_TOKEN", "")
    TEMPLATE_URL = os.environ.get("TEMPLATE_URL", "")
