import os
from flask import Flask, redirect, render_template, request, url_for

from openai_prompts.GPT3_prompts import sandwich_prompt,book_prompt
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        sandwich_toppings = request.form.get("sandwich_toppings")
        temp = float(request.form.get("creativity"))
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=sandwich_prompt(sandwich_toppings),
            temperature=temp,
        )
        return render_template("index.html", result=response.choices[0].text)

    return render_template("index.html")

@app.route("/book_prompts", methods=("GET", "POST"))
def book_prompts():
    
    if request.method == "POST":
        book_topics = request.form.get("book_topics")
        temp = float(request.form.get("creativity"))
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=book_prompt(book_topics),
            temperature=temp,
        )
        return render_template("book_prompts.html", result=response.choices[0].text)

    return render_template("book_prompts.html")


@app.route("/image_maker", methods=("GET", "POST"))
def image_maker():
    if request.method == "POST":
        form_prompt = request.form.get("image_prompt")
        response = openai.Image.create(
            prompt=form_prompt,
            n=1,
            size="512x512",
        )
        return redirect(url_for("image_maker", image_url = response['data'][0]['url']))

    image_url = request.args.get("image_url")
    return render_template("image_maker.html", image_url=image_url)

@app.route("/qna_maker", methods=("GET", "POST"))
def qna_maker():        
    if request.method == "POST":
        question = request.form.get("question")
        temp = float(request.form.get("creativity"))
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=question,
            temperature=temp,
        )
        return render_template("qna_prompt.html", result=response.choices[0].text)

    return render_template("qna_prompt.html")




