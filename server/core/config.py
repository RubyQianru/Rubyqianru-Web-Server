'''
Contains configuration settings for your application.
'''
# server/core/config.py

class Settings:
    DB_URL: str = "postgresql://ruzhang:RZcp1207@localhost/job"

settings = Settings()