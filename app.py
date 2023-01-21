import os

import openai
from flask import Flask, redirect, render_template, request, url_for

secrets = openai_secret_manager.get_secrets("openai")
api_key = secrets["api_key"]


app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
            max_tokens = 4000
        )
        return redirect(url_for("index", result=response.choices.text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )
