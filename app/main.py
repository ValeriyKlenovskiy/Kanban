from fastapi import FastAPI

from app.boards.router import router as boards_router
from app.cards.router import router as cards_router
from app.lists.router import router as lists_router
from app.spaces.router import router as spaces_router
from app.users.router import router as users_router

app = FastAPI()

app.include_router(boards_router)
app.include_router(cards_router)
app.include_router(lists_router)
app.include_router(spaces_router)
app.include_router(users_router)
