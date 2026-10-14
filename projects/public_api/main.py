# | | | --- -- -- -- --- | | |

from datetime import datetime
from random import choice, randint

from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)


# Home page with a clean HTML interface and clickable links
@app.route("/")
def index():
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>My Public API Dashboard</title>
        <style>
            body { font-family: sans-serif; background: #1e1e1e; color: #d4d4d4; padding: 40px; }
            h1 { color: #4ec9b0; }
            .card { background: #252526; padding: 20px; margin-bottom: 15px; border-radius: 8px; border: 1px solid #333; }
            a { display: inline-block; margin-top: 10px; padding: 8px 16px; background: #007acc; color: white; text-decoration: none; border-radius: 4px; }
            a:hover { background: #005999; }
        </style>
    </head>
    <body>
        <h1>Welcome to My Public API</h1>
        <p>Select an endpoint below to test it:</p>
        
        <div class="card">
            <h3>Random Phrase Endpoint</h3>
            <p>Returns a random phrase and current timestamp.</p>
            <a href="/api/phrase">/api/phrase</a>
        </div>

        <div class="card">
            <h3>Random Number Generator</h3>
            <p>Generates a random number up to a specified limit.</p>
            <a href="/api/random?number=50&text=hello">/api/random?number=50&text=hello</a>
        </div>

        <div class="card">
            <h3>Calculator Endpoint</h3>
            <p>Performs basic math operations (add, sub, mul, div).</p>
            <a href="/api/calc?a=15&b=5&op=add">/api/calc?a=15&b=5&op=add</a><br>
            <a href="/api/calc?a=20&b=4&op=div">/api/calc?a=20&b=4&op=div</a><br>
            <a href="/api/calc?a=20&b=4&op=sub">/api/calc?a=20&b=4&op=sub</a><br>
            <a href="/api/calc?a=20&b=4&op=mul">/api/calc?a=20&b=4&op=mul</a><br>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)


# endpoint with random phrases
@app.route("/api/phrase")
def get_phrase():
    phrases: list[str] = [
        "Welcome to this page!",
        "You are looking good today!",
        "The weather is great!",
    ]
    return jsonify({"phrase": choice(phrases), "date": datetime.now().isoformat()})


# endpoint for giving the user back a random number or text if input is nothing
@app.route("/api/random")
def get_random():
    number_input = request.args.get("number", type=int, default=100)
    text_input = request.args.get("text", type=str, default="default_text_here")

    # protection in the form of boundaries
    if isinstance(number_input, int) and 0 < number_input <= 10000:
        return jsonify(
            {
                "input": number_input,
                "random": randint(0, number_input),
                "text": text_input,
                "date": datetime.now().astimezone(),
            }
        )
    else:
        return jsonify({"Error": "Please only enter numbers and positive values."}), 400


# endpoint for calculations
@app.route("/api/calc")
def calculate():
    a = request.args.get("a", default=0, type=float)
    b = request.args.get("b", default=0, type=float)
    op = request.args.get("op", default="add", type=str)

    result = None

    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    elif op == "div":
        if b == 0:
            return jsonify({"Error": "Division by zero is not allowed."}), 400
        result = a / b
    else:
        return jsonify({"Error": "Unknown operation. Use add, sub, mul, or div."}), 400

    return jsonify({"a": a, "b": b, "operation": op, "result": result})


# | | | --- -- -- -- --- | | |


def main() -> None:
    app.run()


if __name__ == "__main__":
    main()


# =============== local ===============
# http://127.0.0.1:5000
# http://127.0.0.1:5000/api/random?number=1000&text=hello
# http://127.0.0.1:5000/api/calc?a=5&b=5&op=mul


# =============== public ===============
# https://meksra.pythonanywhere.com/
# https://meksra.pythonanywhere.com/api/random?number=1000&text=hello
# https://meksra.pythonanywhere.com/api/calc?a=5&b=5&op=mul
#
# (sign up pythonanywhere.com for this host)
# | | | --- -- -- -- --- | | |
# ... (and insert this code on the website)
# | | | --- -- -- -- --- | | |
