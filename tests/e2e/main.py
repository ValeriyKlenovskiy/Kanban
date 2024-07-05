import pytest
import requests

# Todo
# 1) write fixture
# 2) write test_delete_space

URL = "http://localhost/spaces"


@pytest.fixture(scope='function')
def clean_database():
    # code to connect to database
    yield
    # code to clear the database


class Space:
    def __init__(self, space_id, title, allowed_users, ordering, owner=None):
        self.id = space_id
        self.title = title
        self.allowed_users = allowed_users
        self.ordering = ordering
        self.owner_id = owner


def create_space(space):
    if not isinstance(space, Space):
        raise TypeError("Space must be of type Space")

    body = {
        {
            "title": space.title,
            "owner_id": space.owner_id,
            "allowed_users": space.allowed_users,
            "ordering": space.ordering,
            "id": space.id
        }
    }
    response = requests.post(URL, json=body)
    if response.status_code != 200:
        raise requests.exceptions.HTTPError

    return response.json()


def get_spaces():
    response = requests.get(URL)
    if response.status_code != 200:
        raise requests.exceptions.HTTPError

    return response.json()


def update_space(space_id, model):
    if not isinstance(model, Space):
        raise TypeError("Model must be of type Space")

    body = {
        {
            "title": model.title,
            "owner_id": 0,
            "allowed_users": model.allowed_users,
            "ordering": model.ordering,
        }
    }
    response = requests.put(URL + "/" + str(space_id), json=body)
    if response.status_code != 200:
        raise requests.exceptions.HTTPError

    return response.json()


class TestSpaces:
    def test_get_empty_spaces(self):
        """
        Should return empty list
        """
        spaces = get_spaces()
        assert spaces == []

    def test_post_space(self, space_id=0, title="Test space", allowed_users=None, ordering=None):
        """
        Should post new correct space and return it
        """
        if ordering is None:
            ordering = [0]
        if allowed_users is None:
            allowed_users = [0]

        expected_state = [
            {
                "id": space_id,
                "title": title,
                "owner_id": 0,
                "allowed_users": allowed_users,
                "ordering": ordering
            }
        ]

        response = requests.post(URL)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError

        spaces = response.json()

        assert spaces == expected_state

    def test_delete_space(self):
        """
        Should delete correct space
        """
        pass

    def test_update_space_title(self):
        """
        Should update correct space and return it
        """
        space_id = 999
        new_title = "Second title"

        space = Space(space_id, "First title", [0], [1])
        create_space(space)

        edited_space = Space(space_id, new_title, [0], [1])
        updated_space = update_space(space_id, edited_space)

        assert updated_space.title == edited_space.title


class TestModule:
    def test_get_spaces(self):
        """
        Should make and return correct spaces
        """
        spaces = [
            Space(0, "First space", [0], [1], 0),
            Space(0, "Second space", [0], [2], 0),
            Space(0, "Last space", [0], [3], 0),
        ]
        expected_spaces = []

        for index, space in enumerate(spaces):
            create_space(space)
            expected_spaces.append({
                "id": spaces[index].id,
                "title": spaces[index].title,
                "owner_id": spaces[index].owner_id,
                "allowed_users": spaces[index].allowed_users,
                "ordering": spaces[index].ordering
            })

        new_spaces = get_spaces()

        assert new_spaces == spaces
