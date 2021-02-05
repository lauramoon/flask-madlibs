from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story_map

app = Flask(__name__)

app.config['SECRET_KEY'] = "ilovecats"
debug = DebugToolbarExtension(app)

story_title=""

@app.route('/')
def story_select():
    titles = list(story_map.keys())
    return render_template('index.html', titles=titles)

@app.route('/form')
def show_form():
    title = request.args.get('title')
    story = story_map.get(title, "")
    prompts = story.prompts if story else []
    return render_template('form.html', prompts=prompts, title=title)

@app.route('/story')
def show_story():
    title = request.args['title']
    if title in story_map:
        story_text = story_map[title].generate(request.args)
    else:
        story_dict = request.args.to_dict()
        new_story = Story(story_dict.keys(), request.args['template'])
        story_text = new_story.generate(request.args)
    return render_template('story.html', title=title, text=story_text)

@app.route('/new_template')
def new_template():
    return render_template('new_template.html')