import os
from dotenv import load_dotenv

load_dotenv()
class Settings:
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_host: str = os.getenv("DB_HOST")
    db_name: str = os.getenv("DB_NAME")
    db_driver: str = os.getenv("DB_DRIVER")
    db_encrypt: str = os.getenv("DB_ENCRYPT")
    db_trust_server_certificate: str = os.getenv("DB_TRUST_SERVER_CERTIFICATE")
    api_key: str = os.getenv("API_KEY")