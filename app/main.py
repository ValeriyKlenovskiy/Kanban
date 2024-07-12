from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.boards.router import router as boards_router
from app.cards.router import router as cards_router
from app.lists.router import router as lists_router
from app.spaces.router import router as spaces_router
from app.users.router import router as users_router

app = FastAPI()

app.include_router(users_router)
app.include_router(spaces_router)
app.include_router(boards_router)
app.include_router(lists_router)
app.include_router(cards_router)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
