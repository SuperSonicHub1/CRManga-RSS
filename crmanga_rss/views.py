from flask import Blueprint, render_template, abort, Response
from .api import api
from .generator import create_feed

views = Blueprint("views", __name__, url_prefix="/")

@views.route("/")
def index():
	get_title = lambda s: s["locale"]["enUS"]["name"]
	series = map(
		lambda s: dict(title=get_title(s), slug=s["url"][1:]),
		api.list_series()
	)
	return render_template("index.html", series=series)

@views.route("/feed/<slug>")
def feed(slug: str):
	single_series = [
		x
		for x in api.list_series()
		if "/" + slug == x["url"]
	]

	if not single_series:
		abort(404)

	feed = create_feed(single_series[0])

	return Response(feed.rss(), mimetype='application/rss+xml')
