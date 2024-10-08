# app/schemas/book.py
from pydantic import BaseModel

class JobCreate(BaseModel):
    s_title: str
    s_company: str
    s_url: str
    b_apply: bool
    s_tag: str

class JobResponse(BaseModel):
    s_id: str
    s_title: str
    s_company: str
    s_url: str
    b_apply: bool
    s_tag: str
    s_time: str
