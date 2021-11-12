from .api import api
from datetime import datetime
from rfeed import Guid, Item, Feed
from .extensions import WebfeedsIcon, Webfeeds
from functools import partial

def generate_chapter_item(chapter: dict, series: dict):
	try:
		published = datetime.fromisoformat(chapter["availability_start"])
	except ValueError:
		try:
			published = datetime.fromisoformat(chapter["updated"])
		except ValueError:
			try:
				published = datetime.fromisoformat(chapter["published"])
			except ValueError:
				published = None

	chapter_number = float(chapter["number"])
	url_chapter_number = int(chapter_number) if not chapter_number % 1 else chapter_number

	link = f"https://www.crunchyroll.com/manga{series['url']}/read/{url_chapter_number}"

	info = {
		"title": chapter["locale"]["enUS"]["name"],
		"link": link,
		"guid": Guid(link),
		"pubDate": published,
		"author": series["authors"],
	}
	
	return Item(**info)

def create_feed(series: dict):
	chapters = api.list_chapters(series["series_id"])
	
	gen_chapter_partial = partial(generate_chapter_item, series=series)
	
	locale = series["locale"]["enUS"]

	icon_url = locale["full_image_url"]
	icon = WebfeedsIcon(icon_url)

	info = {
		"title": locale["name"],
		"description": locale["description"],
		"link": f"https://www.crunchyroll.com/comics/manga{series['url']}/volumes",
		"items": map(gen_chapter_partial, chapters["chapters"]),
		"extensions": [Webfeeds(),  icon,],
		"lastBuildDate": datetime.now(),
	}

	return Feed(**info)
