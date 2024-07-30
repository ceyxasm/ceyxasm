import markdown
from jinja2 import Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

with open('blog_post.md', 'r', encoding='utf-8') as f:
    content = f.read()

split_content = content.split('---')
metadata = yaml.safe_load(split_content[1])
md_content = split_content[2]

card_open = '<div class="card"><div class="card-block"><div class="row">'
card_close = '</div></div></div>'
col_close = '</div>'

def process_custom_tags(html_content):
    col_mapping = {f'col-{i}': f'<div class="col-md-{i}" style="font-size: 24px;" >' for i in range(1, 13)}

    html_content = html_content.replace('{{card}}', card_open)
    html_content = html_content.replace('{{/card}}', card_close)
    html_content = html_content.replace('{{/col}}', col_close)
    for tag, replacement in col_mapping.items():
        html_content = html_content.replace(f'{{{{{tag}}}}}', replacement)
    return html_content

# Convert Markdown content to HTML
html_content = markdown.markdown(md_content, extensions=['extra', 'smarty', 'sane_lists'])

# Process custom tags in the HTML content
processed_html_content = process_custom_tags(html_content)

# Render the HTML with the template
rendered_html = template.render(
    title=metadata['title'],
    author=metadata['author'],
    content=processed_html_content
)

# Save the rendered HTML to a file
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(rendered_html)
