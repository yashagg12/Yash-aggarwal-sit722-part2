# import os

# class Settings:
#     DATABASE_URL: str= os.getenv('DATABASE_URL')
    
#     settings = Settings()
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

# Initialize settings instance
settings = Settings()
