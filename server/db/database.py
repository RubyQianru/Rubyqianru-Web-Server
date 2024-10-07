from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, schema, Boolean

DB_URL = "postgresql://ruzhang:RZcp1207@localhost/job"

database = Database(DB_URL)
metadata = MetaData()

# Create schema if it doesn't exist
engine = create_engine(DB_URL)
with engine.connect() as conn:
    conn.execute(schema.CreateSchema('public', if_not_exists=True))

jobs = Table(
    "jobs", 
    metadata,
    Column("s_id", Integer, primary_key=True, index=True),
    Column("s_title", String, index=True),
    Column("s_url", String, index=True),
    Column("b_apply", Boolean),
    Column("s_time", String, index=True),
    Column("s_tag", String, index=True),
)

engine = create_engine(DB_URL)
metadata.create_all(engine)