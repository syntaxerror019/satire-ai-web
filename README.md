# Satire AI Web

Small Flask site that renders markdown articles with YAML front matter. The app lives at `api/index.py` and loads content from `api/content/` (markdown files). Templates should be in `api/templates/` and static assets in `api/static/`.

## Features
- Reads markdown files with YAML front matter (using python-frontmatter)
- Renders Markdown to HTML (markdown package) with code highlighting
- Simple search (title/summary)
- Slug generation and date parsing

## Requirements
- Python 3.8+
- Linux environment (commands below assume bash)
- Python packages:
  - flask
  - python-frontmatter
  - markdown
  - pygments (recommended for codehilite)

Install quickly:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask python-frontmatter markdown pygments
```
Or add a requirements.txt with:

```
flask
python-frontmatter
markdown
pygments
```

and run:

```bash
pip install -r 
```

## Run

```bash
# Option A: run module directly
python3 

# Option B: using flask CLI
export 
export FLASK_ENV=development
flask run
```
The app defaults to debug mode when run directly.