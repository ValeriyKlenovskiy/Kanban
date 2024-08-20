from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from app.admin.auth import authentication_backend
from app.admin.view import BoardsAdmin, CardsAdmin, UsersAdmin, ListsAdmin, SpacesAdmin, BackgroundsAdmin, \
    VerificationAdmin, ResetAdmin
from app.boards.router import router as boards_router
from app.cards.router import router as cards_router
from app.database import engine
from app.lists.router import router as lists_router
from app.spaces.router import router as spaces_router
from app.users.router import router as users_router
from app.backgrounds.router import router as backgrounds_router
from app.users.verification.router import router as verification_router
from app.users.password_reset.router import router as password_reset_router


app = FastAPI()


app.include_router(users_router)
app.include_router(spaces_router)
app.include_router(boards_router)
app.include_router(lists_router)
app.include_router(cards_router)
app.include_router(backgrounds_router)
app.include_router(password_reset_router)
app.include_router(verification_router)


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

admin = Admin(app, engine, authentication_backend=authentication_backend)


admin.add_view(UsersAdmin)
admin.add_view(SpacesAdmin)
admin.add_view(BoardsAdmin)
admin.add_view(ListsAdmin)
admin.add_view(CardsAdmin)
admin.add_view(BackgroundsAdmin)
admin.add_view(VerificationAdmin)
admin.add_view(ResetAdmin)
