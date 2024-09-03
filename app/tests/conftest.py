import json
from datetime import datetime

import pytest
from httpx import AsyncClient
from sqlalchemy import insert

from app.boards.models import Boards
from app.backgrounds.models import Backgrounds
from app.cards.models import Cards
from app.config import settings
from app.database import Base, async_session_maker, engine

from app.lists.models import Lists
from app.main import app as fastapi_app
from app.spaces.models import Spaces
from app.users.models import Users


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"app/tests/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)

    users = open_mock_json("users")
    spaces = open_mock_json("spaces")
    backgrounds = open_mock_json("backgrounds")
    boards = open_mock_json("boards")
    lists = open_mock_json("lists")
    cards = open_mock_json("cards")


    for lst in lists:
        lst["date_added"] = datetime.strptime(lst["date_added"], "%Y-%m-%d")

    for card in cards:
        card["date_added"] = datetime.strptime(card["date_added"], "%Y-%m-%d")
        card["deadline"] = datetime.strptime(card["deadline"], "%Y-%m-%d")

    async with async_session_maker() as session:
        for Model, values in [
            (Users, users),
            (Spaces, spaces),
            (Backgrounds, backgrounds),
            (Boards, boards),
            (Lists, lists),
            (Cards, cards),
        ]:
            query = insert(Model).values(values)
            await session.execute(query)

        await session.commit()




@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="session")
async def authenticated_ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        await ac.post(
            "/users/login",
            json={
                "email": "test@test.com",
                "password": "test",
            },
        )
        assert ac.cookies["kanban_access_token"]
        yield ac