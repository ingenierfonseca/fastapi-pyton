from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from settings import Settings


#DATABASE_URL = "mssql+pyodbc://localhost/UpciDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
#DATABASE_URL = (
    #"mssql+pyodbc://db_a827be_factinventario_admin:Invetfact24*@SQL5113.site4now.net/db_a827be_factinventario"
    #"?driver=ODBC+Driver+17+for+SQL+Server&encrypt=yes&trustServerCertificate=yes"
#)
settings = Settings()

DATABASE_URL = (
    f"mssql+pyodbc://{settings.db_user}:{settings.db_password}@{settings.db_host}/{settings.db_name}"
    f"?driver={settings.db_driver}&encrypt={settings.db_encrypt}&trustServerCertificate={settings.db_trust_server_certificate}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependencia
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()