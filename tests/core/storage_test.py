from bapi.core.storage import storage
import pytest
from bapi.core.exception import BapiException

def test_load_ok():
    storage.load('tests/data/example.beancount')

def test_load_not_exists():
    with pytest.raises(BapiException):
        storage.load('tests/data/nosuchfile.beancout')
