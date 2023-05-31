from sqlalchemy import create_engine
from sqlalchemy.sql import text
from src.models.model import Person

def read_data():
    engine = create_engine('sqlite:///person.db')
    with engine.connect() as con:
        satement = text(f"""SELECT * FROM person""")
        con.execute(satement)
        result = con.execute(satement)
        data = result.fetchone()
    return Person(**data)