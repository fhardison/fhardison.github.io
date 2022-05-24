import markdown
from pathlib import Path

def load_template(name):
    with open(Path(f'./templates/{name}'), 'r', encoding="UTF-8") as f:
        return f.read()


def inject_bits(template, body, meta='', nav=''):
    return template.replace('@@NAV@@', nav).replace('@@META@@', meta).replace('@@BODY@@', body)

TEMPLATE = load_template('template.html')
HEADER = load_template('header.html')

print(inject_bits(TEMPLATE, '', nav=HEADER))
md = markdown.Markdown(extensions=['meta'])

POSTS = []
POSTPATH = Path('./posts/')


def make_meta(metadata):
    output = []
    if 'title' in metadata:
        output.append(f"<title>{metadata['title']}</title>")
    if 'author' in metadata:
        output.append(f"<meta name='author'>{metadata['author']}</meta>")
    return '\n'.join(output)

def load_posts(postPath, processor, template):
    output = []
    for x in POSTPATH.glob('**/*.md'):
        htmlPath = str(x).replace('.md', '.html').replace('posts', 'docs')
        with open(x, 'r', encoding="UTF-8") as f, open(htmlPath, 'w', encoding="UTF-8") as g:
            md = f.read()
            html = processor.convert(md)
            meta = make_meta(processor.Meta)
            g.write(template(html, meta))
            print(processor.Meta['title'])
            output.append((processor.Meta['title'][0], htmlPath))
    return output

posts = load_posts(POSTPATH, md, lambda x, y: inject_bits(TEMPLATE, x, meta=y, nav=HEADER))

def fix_link(link):
    return link[link.index('docs') + 4:].replace('\\', '/')

with open('contents.md', 'r', encoding="UTF-8") as f, open(Path('./docs/index.html'), 'w', encoding="UTF-8") as g:

    formatted_posts = '\n'.join([f"<li><a href='{fix_link(link)}'>{title}</a></li>" for (title, link) in posts])
    wrapped = f"""<ul>
    {formatted_posts}
    </ul>"""
    
    contents = f.read().replace('@@POSTS@@', formatted_posts)

    g.write(inject_bits(TEMPLATE, md.convert(contents), nav=HEADER))

print("DONE")




