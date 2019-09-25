from flask import Flask, render_template, request
import getRichOrDieTrying.Order

app = Flask(__name__)


@app.route("/profile/<username>/<int:id_number>",
           methods=["GET", "POST"])  # the user will ask for this web-page where the user should enter the variable
# username and id_number
def profile(username, id_number):
    return render_template("profile.html", username=username, id_number=id_number)


if __name__ == "__main__":
    app.run(debug=True)
