# app.py

from flask import Flask
app = Flask(__name__)
# This is a test commit
# new commit
def add(a, b):
    # to test personal alert, uncoment below code
    # return a + b + 100 
    return a + b
    # run the below code to test slack email notification on pipeline failure
    # return a + b + 100

@app.route('/')
def home():
    result = add(10, 20)
    return f"<h1>DevOps Project: Success! Ayushiiiii</h1><p>10 + 20 = {result}</p>"
    
def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

# Add this to see output in your terminal
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
