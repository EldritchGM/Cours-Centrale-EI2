# content of test_some_are_slow.py
import time, pytest

@pytest.mark.skip("no test")
def test_funcfast():
    time.sleep(0.1)
def test_funcslow1():
    time.sleep(0.2)
def test_funcslow2():
    time.sleep(0.3)