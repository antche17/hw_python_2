import pytest




@pytest.fixture
def login_page(browser):
    print("Логин пейдж")
    pass

@pytest.fixture
def user():
    print("Юзернэйм")
    return "username", "password"


def test_login(login_page, user):
    username, password =user
    assert username == "username"
    assert password == "password"