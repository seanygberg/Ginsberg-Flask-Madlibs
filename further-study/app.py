from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)

@app.route("/")
def ask_story():
    result = stories.values()
    return render_template("select-story.html",
                           stories=result)

@app.route("/questions")
def ask_questions():
    s_id = request.args["story_id"]
    story = stories[s_id]
    prompts = story.prompts
    return render_template("questions.html",
                           story_id=story_id,
                           title=story.title,
                           prompts=prompts)

@app.route("/story")
def show_story():
    s_id = request.args["story_id"]
    story = stories[s_id]

    text = story.generate(request.args)

    return render_template("story.html",
                           title=story.title,
                           text=text)