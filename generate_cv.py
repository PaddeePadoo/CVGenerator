import markdown
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
import re

def parse_markdown(md_file):
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content, extensions=["fenced_code", "tables"])
    return html_content


def extract_sections(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    sections = {
        "header": "", "title": "", "contact": "", "summary": "",
        "skills": "", "work_experience": "", "education": "",
        "languages": "", "interests": ""
    }

    current_section = None
    current_subsection = None
    work_experience_html = ""

    for tag in soup.find_all(["h1", "h2", "h3", "p", "ul", "li"]):
        if tag.name == "h1":
            sections["header"] = str(tag)  # Keep full HTML structure
        elif tag.name == "p" and "Email" in tag.text:
            sections["contact"] = str(tag)
        elif tag.name == "h2":
            current_section = tag.text.lower().replace(" ", "_")
            if current_section in sections:
                sections[current_section] = str(tag)  # Preserve heading
        elif tag.name == "h3" and current_section == "work_experience":
            if current_subsection:
                work_experience_html += "</div>"  # Close previous job div
            current_subsection = tag.text
            work_experience_html += f"<div class='job'><h3>{current_subsection}</h3>"
        elif tag.name in ["p", "ul"]:
            if current_section == "work_experience":
                work_experience_html += str(tag)
            else:
                sections[current_section] += str(tag)

    if current_subsection:
        work_experience_html += "</div>"  # Close last job div

    # Assign the work experience content correctly to the section
    if work_experience_html:
        sections["work_experience"] = f"<h2>Work Experience</h2>{work_experience_html}"

    return sections

def strip_html(value):
    """Remove HTML tags from the string."""
    return re.sub(r'<.*?>', '', value)

env = Environment(loader=FileSystemLoader("."))
env.filters['strip_html'] = strip_html  # Register the custom filter


def generate_cv(md_file, output_html, template_file):
    env = Environment(loader=FileSystemLoader("."))
    env.filters['strip_html'] = strip_html  # Register the filter
    template = env.get_template(template_file)

    html_content = parse_markdown(md_file)
    sections = extract_sections(html_content)

    rendered_html = template.render(
        name=sections["header"],
        contact=sections["contact"],
        summary=sections["summary"],
        skills=sections["skills"],
        work_experience=sections["work_experience"],
        education=sections["education"],
        languages=sections["languages"],
        interests=sections["interests"],
    )

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(rendered_html)


if __name__ == "__main__":
    generate_cv("example_cv.md", "cv_output.html", "cv_template.html")
