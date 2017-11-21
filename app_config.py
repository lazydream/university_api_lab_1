class BaseConfig:
    DEBUG = False
    TESTING = False


class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = True
