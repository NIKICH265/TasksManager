from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    DATABASE_PATH: str = "database.db"
    DEBUG: bool = False


    @property
    def db_path(self) -> str:
        return f"sqlite:///{self.DATABASE_PATH}"


settings = Settings()
