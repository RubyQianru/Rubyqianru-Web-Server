from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, schema

DB_URL = "postgresql://ruzhang:RZcp1207@localhost/books"

database = Database(DB_URL)
metadata = MetaData()

# Create schema if it doesn't exist
engine = create_engine(DB_URL)
with engine.connect() as conn:
    conn.execute(schema.CreateSchema('public', if_not_exists=True))

books = Table(
    "books", 
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String, index=True),
    Column("author", String, index=True),
    Column("price", Float),
)

engine = create_engine(DB_URL)
metadata.create_all(engine)