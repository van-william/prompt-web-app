import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        sandwich_toppings = request.form["sandwich_toppings"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(sandwich_toppings),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(sandwich_toppings):
    return """Suggest three names for a custom sandwich order.

Sandwich Toppings: Genoa Salami, Capocollo,Provolone, Hot Peppers, onion, lettuce, tomato & easy mayo
Sandwich Name: Spicy East Coast Italian
Sandwich Toppings: Turkey, Provolone, Avocado, cucumber, lettuce, tomato & mayo
Sandwich Name: Beach Club
Sandwich Toppings: a biscuit, a piece of fried chicken, and some sausage gravy
Sandwich Name: The East Nasty
Sandwich Toppings: {}
Sandwich Name:""".format(
        sandwich_toppings.capitalize()
    )
