from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="Fast API LMS",
    description= "LOL",
    version= "0.0.1",
    contact={
        "name": "Xing Gao",
        "email": "2222@qq.com"
    },
    license_info={
        "name": "BYUI"
    }
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_user():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return 'Success'


@app.get("/users/{id}")
# ... show that it is required
async def get_user(
    id: int = Path(..., description="The ID of the user you want to retrieve.", gt=0),
    q: str = Query(None, max_length=5)
    ):
    return {"users": users[id], "query": q}