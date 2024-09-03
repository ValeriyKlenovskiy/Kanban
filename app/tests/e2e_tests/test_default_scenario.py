from datetime import date

import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("title, status_code", [
    ("asf",  200),
    ("assaffa112f", 200)
])
async def test_add_space(
        title: str,
        status_code: int,
        authenticated_ac: AsyncClient,
):
    response = await authenticated_ac.post(
        "/spaces",
        json={
            "title": title,
        })
    assert response.status_code == status_code


@pytest.mark.parametrize("title, space_id, background_id, status_code", [
    ("asf",  1, 1, 200),
    ("assaffa112f", 11, 2, 200),
    ("assaffa112f", 2123, 3, 500)
])
async def test_add_board(
        title: str,
        space_id: int,
        background_id: int,
        status_code: int,
        authenticated_ac: AsyncClient,
):
    response = await authenticated_ac.post(
        "/boards",
        json={
            "title": title,
            "space_id": space_id,
            "background_id": background_id
        })
    assert response.status_code == status_code


@pytest.mark.parametrize("title, board_id, description, date_added, status_code", [
    ("asf",  1, "afas", "2024-12-11", 200),
    ("sadasfaf",  2, "afasasdasd", "2024-12-11", 200),
    ("asf", 111, "afas", "2024-12-11", 500),
    ("asf", 11, 1, "2024-12-11", 422),
    ("asf",  3, "afas", "2024-12-1111", 422),
])
async def test_add_list(
        title: str,
        board_id: int,
        description: str,
        date_added: date,
        status_code: int,
        authenticated_ac: AsyncClient,
):
    response = await authenticated_ac.post(
        "/lists",
        json={
            "title": title,
            "board_id": board_id,
            "description": description,
            "date_added": date_added,
        })
    assert response.status_code == status_code


@pytest.mark.parametrize("title, list_id, description, date_added, labels, deadline, status_code", [
    ("asf",  1, "afas", "2024-12-11", "asd", "2024-12-11", 200),
    ("sadasfaf",  2, "afasasdasd", "2024-12-11", "asd", "2024-12-21", 200),
    ("asf", 111, "afas", "2024-12-11", "asd", "2024-12-11", 500),
    ("asf", 11, 1, "2024-12-11", "asd", "2024-12-11", 422),
    ("asf",  3, "afas", "2024-1212-11", "asd", "2024-12-11", 422),
    ("asf", 3, "afas", "2024-12-11", 1, "2024-12-11", 422),
    ("asf", 3, "afas", "2024-12-11", "asd", "2024-1213-11", 422),
    ("asf", 3, "afas", "2024-12-11", "asd", "2024-11-11", 409),
])
async def test_add_card(
        title: str,
        list_id: int,
        description: str,
        date_added: date,
        labels: str,
        deadline: date,
        status_code: int,
        authenticated_ac: AsyncClient,
):
    response = await authenticated_ac.post(
        "/cards",
        json={
            "title": title,
            "list_id": list_id,
            "description": description,
            "date_added": date_added,
            "labels": labels,
            "deadline": deadline,
        })
    assert response.status_code == status_code
