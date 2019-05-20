import os

class Config:
    """
    Main configurations class. Acts a a parent configuration class
    """

    NEWS_API_KEY = '065ac49d6df4496d8e9b6596749a6fdd'
    


class ProdConfig(Config):
    """
    Production configuration class that inherits from the main configurations class
    """
    pass


class DevConfig(Config):
    """
    Configuration class for development stage of the app that inheits from the main class
    """
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
