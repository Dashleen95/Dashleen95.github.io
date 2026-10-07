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

## CV and papers

The current CV is in `files/CV_Kaur_Dashleen.pdf` and available from About and CV.
Research is ordered as Job Market Paper, Working Papers, Work in Progress, and
Book Chapters. The published chapter links to LSE Press.

Working paper entries use a month/year, Working Paper, [Abstract], [PDF] row.
Abstract buttons show or hide the corresponding text below each entry. The job
market paper’s two resource labels remain inactive until its draft and abstract
are supplied. The tutoring PDF is the August 2025 Phase 1 conference draft at
`files/peer-tutoring-phase1.pdf`.

The judiciary working paper uses the stable path `files/politicized-judiciary.pdf`.
To publish a revised draft, replace this PDF at the same path, rebuild, and deploy.
The website link will stay the same. This copy does not sync automatically with
the original attachment or a local editing folder.

For updates without rebuilding the website, replace the judiciary title and PDF
links in `_pages/research.html` with a shared link to the paper in Dropbox. Upload
each revised PDF with the same filename to the same folder on dropbox.com,
overwriting the existing file. Do not delete and recreate it. A Dropbox source
has not yet been connected.

The ChatGPT Sites copy starts private. GitHub Pages publication is separate.
