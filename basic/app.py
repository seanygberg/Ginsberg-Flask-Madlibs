from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route("/")
def ask_questions():
    prompts = story.prompts
    result = render_template("index.html", prompts=prompts)
    return result

@app.route("/story")
def show_story():
    text = story.generate(request.args)
    result = render_template("story.html", text=text)
    return result