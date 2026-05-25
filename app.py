from flask import Flask, render_template, redirect, request
import json

app = Flask(__name__)

with open("data/stories.json") as file:
    stories = json.load(file)


@app.route("/")
def home():

    return render_template(
        "index.html",
        stories=stories
    )


@app.route("/story/<int:story_id>")
def story(story_id):

    xp = request.args.get(
        "xp",
        default=0,
        type=int
    )

    unlock_requirements = {
        1: 0,
        2: 50,
        3: 100,
        4: 150,
        5: 200,
        6: 250
    }

    required_xp = unlock_requirements.get(
        story_id,
        999
    )

    if xp < required_xp:

        return redirect("/")

    selected_story = None

    for s in stories:

        if s["id"] == story_id:

            selected_story = s
            break

    if not selected_story:

        return redirect("/")

    return render_template(
        "story.html",
        story=selected_story
    )


if __name__ == "__main__":

    app.run(debug=True)