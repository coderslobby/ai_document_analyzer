from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Setting(BaseSettings):
    GROQ_API_KEY : str
    language_model : str
    uploadFolder : str
    allowedFileTypes : List[str]
    chunk_size: int
    chunk_overlap: int
    model_config = SettingsConfigDict(
        env_file= '.env',
        env_file_encoding= 'utf-8'
    )

config_setting = Setting() #type: ignore