import os 
from dotenv import load_dotenv 
from sqlmodel import create_engine, SQLModel, Session

load_dotenv()

user = os.getenv("USER")

senha = os.getenv("SENHA")
DATABASE_URL = f"mssql+pyodbc://{user}:{senha}@DIGASPC/PicPaySimplificado?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DATABASE_URL, echo = True)