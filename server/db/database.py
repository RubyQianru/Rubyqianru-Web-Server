from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, schema, Boolean
from server.core.config import settings

DB_URL = settings.DB_URL

database = Database(DB_URL)
metadata = MetaData()

engine = create_engine(DB_URL)
with engine.connect() as conn:
    conn.execute(schema.CreateSchema('public', if_not_exists=True))

jobs = Table(
    "jobs", 
    metadata,
    Column("s_id", String, primary_key=True, index=True),
    Column("s_title", String, index=True),
    Column("s_company", String, index=True),
    Column("s_url", String, index=True),
    Column("b_apply", Boolean),
    Column("s_time", String, index=True),
    Column("s_tag", String, index=True),
    schema='public'
)

github = Table(
    "github", 
    metadata,
    Column("s_id", String, primary_key=True, index=True),
    Column("s_title", String, index=True),
    Column("s_full_name", String, index=True),
    Column("s_desc", String, index=True),
    Column("s_url", String, index=True),
    Column("b_fork", Boolean),
    Column("s_created_at", String, index=True),
    Column("s_updated_at", String, index=True),
    schema='public'
)

metadata.create_all(engine)