from flask import Flask
app=Flask(__name__)
@app.route("/company")
def company_api():
    return [{"Name":"Open AI",
            "Location":"USA",
            "employees":1000}]
app.run(host="0.0.0.0",port=8000,debug=True)
print("Server is running on http://0.0.0.0:8000")