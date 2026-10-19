from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App
    APP_NAME: str = "LUST8 API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Database - SQLite by default
    DATABASE_URL: str = "sqlite:///./lust8.db"

    # Auth
    SECRET_KEY: str = "lust8-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    # CORS
    CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
    ]

    # Pagination
    DEFAULT_PAGE_SIZE: int = 12
    MAX_PAGE_SIZE: int = 100

    class Config:
        env_file = ".env"


settings = Settings()
