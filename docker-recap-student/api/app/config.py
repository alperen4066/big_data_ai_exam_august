from typing import Any, Dict, Optional

from pydantic import validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MYSQL_HOST: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_PORT: str
    API_VERSION_STR: str = "/api/v1"
    SECRET_KEY: str = "SG9wZWxpamsgZ2VicnVpa3QgZWVuIHN0dWRlbnQgZGl0IG9vaXQgbnV0dGlnLg=="
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10

    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return f"mysql+mysqlconnector://{values.get('MYSQL_USER')}:{values.get('MYSQL_PASSWORD')}@{values.get('MYSQL_HOST')}:{values.get('MYSQL_PORT')}/{values.get('MYSQL_DATABASE')}"

    class Config:
        case_sensitive = True

settings = Settings()
