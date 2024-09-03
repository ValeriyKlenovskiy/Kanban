import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("email,password,status_code", [
    ("asdasd@asd.com", "asdasd", 200),
    ("asdasd@asd.com", "asdqw", 409),
    ("wqe@wqe.com", "wqewqe", 200),
    ("abcde", "weqweq", 422),
])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/users/register", json={
        "email": email,
        "password": password,
    })

    assert response.status_code == status_code


@pytest.mark.parametrize("email,password,status_code", [
    ("asdasd@asd.com", "asdasd", 200),
    ("tellus.id@icloud.net", "string", 200),
    ("sad", "asd1", 422),
    ("wrong@person.com", "a123s", 401),
])
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/users/login", json={
        "email": email,
        "password": password,
    })

    assert response.status_code == status_code