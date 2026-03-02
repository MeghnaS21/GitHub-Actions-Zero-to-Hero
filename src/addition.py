# app.py
# This is a test commit
# new commit
def add(a, b):
    return a + b + 100 # to test personal alert
    # run the below code to test slack email notification on pipeline failure
    # return a + b + 100

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
