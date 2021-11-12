# Crunchyroll Manga RSS

[Giving you the subscription button you always wanted][angry_comment].

Steals code from:
- https://replit.com/@SuperSonicHub1/MangaKache
- https://replit.com/@SuperSonicHub1/YouTubeArticle

## Install
```bash
poetry install
# For the lazy...
python3 main.py 
# For the more upstanding
gunicorn 'crmanga_rss:create_app()'
```

[angry_comment]: https://www.crunchyroll.com/comics/manga/attack-on-titan/comments#guestbook_comment_t5429530
