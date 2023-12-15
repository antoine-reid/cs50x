from flask import Flask, render_template, redirect, request, Response, abort
from functools import wraps
import json
from music_theory import Music_Theory

# Configure application
app = Flask(__name__)


def returns_json(f):
    """ Create our own decorator, to change content-type for JSON responses """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        r = f(*args, **kwargs)
        return Response(r, content_type='application/json')
    return decorated_function


@app.after_request
def after_request(response):
    """ Ensure responses are not cached """
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Main page, with circle of fifths and scales
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # We are called with POST when the user clicked on the "Reset" link.
        # Redirect to force a GET on this page, so a refresh of the browser does not ask to resubmit the form.
        return redirect("/")
    return render_template("scales.html")


# Page with chord selection
@app.route("/chords", methods=["GET", "POST"])
def chords_page():
    return render_template("chords.html")


# About page
@app.route("/about")
def about_page():
    return render_template("about.html")


# Get the notes of a specific scale (AJAX)
@app.route("/scale/<s>/<t>")
@returns_json
def scale(s=None, t=None):
    try:
        return json.dumps(Music_Theory.get_scale(s, t))
    except ValueError:
        abort(404)


# Get the diatonic chords of a specific scale (AJAX)
@app.route("/diatonic_chords/<s>/<t>")
@returns_json
def diatonic_chords(s=None, t=None):
    try:
        return json.dumps(Music_Theory.get_diatonic_chords(s, t))
    except ValueError:
        abort(404)


# Get the notes of a specific chord (AJAX)
@app.route("/chord/<chord>")
@returns_json
def chord(chord=None):
    try:
        return json.dumps(Music_Theory.get_chord_notes(chord))
    except ValueError:
        abort(404)
