
from flask import Flask, request, render_template
from ultronex_core.engine import get_ultronex_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = get_ultronex_response(prompt)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=False)
