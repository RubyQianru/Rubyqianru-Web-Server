from pydantic import BaseModel

class GithubCreate(BaseModel):
    name: str
    full_name: str
    description: str = None
    html_url: str
    fork: bool = False
    created_at: str
    updated_at: str

class GithubResponse(BaseModel):
    s_id: str
    s_title: str
    s_full_name: str 
    s_desc: str
    s_url: str
    b_fork: bool
    s_created_at: str
    s_updated_at: str
