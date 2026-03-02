# app.py
# This is a test commit
# new commit
def add(a, b):
    # to test personal alert, uncoment below code
    # return a + b + 100 
    return a + b
    # run the below code to test slack email notification on pipeline failure
    # return a + b + 100

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

# Add this to see output in your terminal
if __name__ == "__main__":
    result = add(5, 5)
    print(f"The server says: 5 + 5 is {result}!")
