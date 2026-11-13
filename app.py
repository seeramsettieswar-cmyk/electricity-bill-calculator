from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_bill(units):

    bill = 0

    if units <= 100:
        bill = units * 2

    elif units <= 200:
        bill = (100 * 2) + ((units - 100) * 3)

    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    else:
        bill = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

    return bill


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():

    name = request.form["name"]
    consumer = request.form["consumer"]
    units = float(request.form["units"])
    connection = request.form["connection"]

    bill = calculate_bill(units)

    result = {
        "name": name,
        "consumer": consumer,
        "units": units,
        "connection": connection,
        "bill": bill
    }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
