"""
Resources:
* https://www.geeksforgeeks.org/flask-app-routing/
* https://www.geeksforgeeks.org/flask-http-methods-handle-get-post-requests/
* https://www.linode.com/docs/guides/create-restful-api-using-python-and-flask/
* https://www.w3schools.com/python/python_datetime.asp
"""
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.get('/api')
def api():
    current = datetime.datetime.now()
    return jsonify(
        {
            "slack_name": request.args['slack_name'],
            "current_day": current.strftime("%A"),
            "utc_time": current.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "track": request.args['track'],
            "github_file_url": "https://github.com/chinweibegbu/zuri-internship/blob/main/stage1/task1.py",
            "github_repo_url": "https://github.com/chinweibegbu/zuri-internship.git",
            "status_code": "200"
        }
    )

@app.route('/')
def index():
    return "Hello, Every-nyan!"
  
if __name__ == "__main__":
    app.run(debug=True)