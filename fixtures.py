import pytest
from server import Server


@pytest.fixture(scope='module', autouse=True)
def object_class_server():
    object_class = Server("https://nominatim.openstreetmap.org/")
    yield object_class
