from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#DATABASE_URL = "mssql+pyodbc://localhost/UpciDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
DATABASE_URL = (
    "mssql+pyodbc://db_a827be_factinventario_admin:Invetfact24*@SQL5113.site4now.net/db_a827be_factinventario"
    "?driver=ODBC+Driver+17+for+SQL+Server&encrypt=yes&trustServerCertificate=yes"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()