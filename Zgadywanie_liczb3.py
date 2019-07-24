from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():

    min = 0
    max = 1000

    result = round(int(max - min) / 2 + min, 0)

    if request.method == "POST":
        more = request.form["more"]
        less = request.form["less"]
        bullseye = request.form["bullseye"]

        # if more:
        #     min = result
        # elif less:
        #     max = result
        # elif bullseye:
        #     print("Wygrałem")

    ctx = {
        'result': result
    }
    return render_template('template_to_4.html',
                           context=ctx)


if __name__ == "__main__":
    app.run(debug=True)
