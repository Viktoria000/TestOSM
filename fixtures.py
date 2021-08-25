import pytest
from server import ServerConnection


@pytest.fixture(scope='module', autouse=True)
def object_class_server():
    object_class = ServerConnection("https://nominatim.openstreetmap.org/")
    yield object_class

