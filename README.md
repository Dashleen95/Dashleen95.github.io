# Dashleen Kaur’s academic website

Adapted from Tushar Kundu’s Jekyll-Uno site, with About, Research, CV, and Contact
pages. The MIT theme license is preserved in LICENSE.

## Update content

- Home biography: `index.html`
- Research: `_pages/research.html`
- Teaching: `_pages/teaching.html`
- CV summary: `_pages/cv.html`
- Contact: `_pages/contact.html`
- Sidebar: `_includes/header.html`
- Styling: `css/site.css`
- Site metadata: `_config.yml` (JSON, which is valid YAML)

## Build

Run `python3 scripts/build.py`. No third-party packages are needed.
It writes the complete static website to `dist/`. Sources are also compatible
with native Jekyll, using the provided configuration, includes, and layouts.

## GitHub Pages

The included workflow builds and deploys `dist/`. Enable GitHub Actions as the
repository’s Pages source. For a personal root URL, name the repository
`YOUR_USERNAME.github.io`. For a project URL, set `baseurl` in `_config.yml`
to the repository path and `url` to your GitHub Pages origin.


