import pytest

from app.users.dao import UsersDAO


@pytest.mark.parametrize("email,is_present", [
    ("et@icloud.ca", True),
    ("quisque.nonummy@outlook.com", True),
    ("jg", False)
])
async def test_find_user_by_id(email, is_present):
    user = await UsersDAO.find_one_or_none(email=email)

    if is_present:
        assert user
        assert user["email"] == email
    else:
        assert not user

