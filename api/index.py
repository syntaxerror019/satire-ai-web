from flask import Flask, render_template, abort, send_from_directory, request, url_for
from pathlib import Path
import frontmatter
import markdown
from datetime import datetime
import re

BASE = Path(__file__).parent
CONTENT_DIR = BASE / "content"

app = Flask(__name__)

# config
MD_EXTENSIONS = [
    'fenced_code',
    'codehilite',
    'toc',
    'tables',
]

def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9-]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s

def read_articles():
    articles = []
    for md_file in CONTENT_DIR.glob("*.md"):
        post = frontmatter.load(md_file)
        meta = post.metadata or {}
        title = meta.get('title') or md_file.stem
        date_raw = meta.get('date')
        
        if isinstance(date_raw, str):
            date = datetime.fromisoformat(date_raw)
        elif isinstance(date_raw, datetime):
            date = date_raw
        else:
            date = datetime.now()
        
        print("DATE PARSED:", date)
        print("DATE RAW:", date_raw)

        html = markdown.markdown(post.content, extensions=MD_EXTENSIONS)
        summary = meta.get('summary') or (post.content.split('\n', 1)[0][:200] + '...')
        author = meta.get('author', 'Staff Writer')
        image = meta.get('image')
        tags = meta.get('tags', [])
        slug = meta.get('slug') or slugify(title)

        articles.append({
            'title': title,
            'date': date,
            'date_str': date.strftime('%B %d, %Y'),
            'author': author,
            'summary': summary,
            'content_html': html,
            'slug': slug,
            'image': image,
            'tags': tags,
            'source_file': md_file.name,
        })

    # sort newest first
    articles.sort(key=lambda a: a['date'], reverse=False)
    return articles


@app.context_processor
def inject_site_info():
    return dict(site_name='The Neural Times', tagline='Your only source of news.', year=datetime.now().year)


@app.route('/')
def index():
    q = request.args.get('q', '').strip()
    page = int(request.args.get('page', 1))  # current page
    per_page = 8  # articles per page

    articles = read_articles()
    if q:
        qlow = q.lower()
        articles = [a for a in articles if qlow in a['title'].lower() or qlow in a['summary'].lower()]

    # Pagination logic
    total = len(articles)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_articles = articles[start:end]

    # Calculate total pages
    total_pages = (total + per_page - 1) // per_page

    return render_template(
        'index.html',
        articles=paginated_articles,
        q=q,
        page=page,
        total_pages=total_pages
    )


@app.route('/article/<slug>')
def article(slug):
    articles = read_articles()
    for a in articles:
        if a['slug'] == slug:
            return render_template('article.html', article=a)
    abort(404)


@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory(BASE / 'static', path)


if __name__ == '__main__':
    app.run(debug=True)
