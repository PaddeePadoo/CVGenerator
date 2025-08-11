# CVGenerator

A simple Python tool to generate a styled CV/resume from a Markdown file using a customizable HTML template.

---

## Features

- Converts structured Markdown CV content into clean HTML output.
- Uses `markdown` and `BeautifulSoup` to parse and extract CV sections.
- Uses `jinja2` templating for flexible CV layout and styling.
- Supports typical CV sections: header, contact, summary, skills, work experience, education, languages, interests.
- Easily customize the CV look by editing the HTML template.
- Comes with an example Markdown CV file for quick testing.

---

## Requirements

- Python 3.x
- `markdown` package
- `beautifulsoup4` package
- `jinja2` package

You can install dependencies via:

```bash
pip install -r requirements.txt
```

## Usage
1. Prepare your CV content in Markdown format (e.g., example_cv.md). Follow the section headings used in the example for best results.
2. Run the generator:
```bash
python generate_cv.py
```
This will read `example_cv.md`, render it using `cv_template.html`, and output `cv_output.html`.
3. Open `cv_output.html` in any browser to view your formatted CV.

## How it works

- The script parses your Markdown content into HTML.
- It extracts CV sections by looking for specific Markdown headers (e.g., `#`, `##`, `###`).
- Work experience subsections are grouped under their job titles.
- The extracted content is injected into the HTML template via Jinja2.
- The template uses CSS for basic layout and styling.

## Customization

- Modify `cv_template.html` to change the CV design or add new sections.
- Adjust or extend `generate_cv.py` to support additional Markdown sections or different HTML output.

## Example

The repository includes `example_cv.md` demonstrating the supported Markdown structure and section formatting.