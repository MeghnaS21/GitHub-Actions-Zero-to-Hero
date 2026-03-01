# app.py
# This is a test commit
# For testing pipelines on actions, I am creating this PR
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
