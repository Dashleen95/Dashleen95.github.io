"""Build this site's small Liquid subset without installing Jekyll.
JSON is valid YAML; the same sources also work with native Jekyll.
"""
from pathlib import Path
import html
import json
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dist"
SITE = json.loads((ROOT / "_config.yml").read_text())

def render(template, context):
    def include(match):
        return render((ROOT / "_includes" / match[1]).read_text(), context)
    template = re.sub(r"{%\s*include\s+([\w.-]+)\s*%}", include, template)
    def variable(match):
        key = match[1].strip()
        value = context
        for part in key.split("."):
            value = value[part]
        return str(value) if key == "content" else html.escape(str(value), quote=True)
    return re.sub(r"{{\s*([\w.]+)\s*}}", variable, template)

def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    layout = (ROOT / "_layouts/default.html").read_text()
    pages = [ROOT / "index.html", *sorted((ROOT / "_pages").glob("*.html"))]
    for source in pages:
        _, metadata, content = source.read_text().split("---", 2)
        page = json.loads(metadata)
        destination = OUT / page["permalink"].strip("/") / "index.html"
        destination.parent.mkdir(parents=True, exist_ok=True)
        content = render(content.strip(), {"site": SITE, "page": page})
        document = render(layout, {"site": SITE, "page": page, "content": content})
        active = page["slug"]
        document = document.replace(f'class="nav-{active}"', f'class="nav-{active}" aria-current="page"')
        if "{%" in document or "{{" in document:
            raise ValueError(f"Unresolved template syntax in {source}")
        destination.write_text(document)
        print(f"Built {page['permalink']}")
    shutil.copytree(ROOT / "images", OUT / "images")
    shutil.copytree(ROOT / "files", OUT / "files")
    (OUT / "css").mkdir()
    shutil.copy(ROOT / "css/site.css", OUT / "css/site.css")
    shutil.copy(ROOT / "LICENSE", OUT / "LICENSE")
    (OUT / ".nojekyll").touch()
    (OUT / "404.html").write_text(render(layout, {"site": SITE, "page": {"slug":"not-found","meta_title":"Page not found | Dashleen Kaur","meta_description":"This page could not be found."}, "content": '<div class="eyebrow">404</div><h1>Page not found.</h1><p><a href="/">Return to the home page</a>.</p>'}))

if __name__ == "__main__":
    main()
