from pathlib import Path
import yaml
import os

script_dir = Path(__file__).parent.absolute()
blog_dir = (script_dir / Path('blog'))
projects_dir = (script_dir / Path('projects'))

def extract_yaml(x):
    raw = Path(x).read_text()
    if '---' not in raw:
        return None
    text = raw.strip().split('---')[1]
    return yaml.safe_load(text)


def walk_tree(x):
    output = []
    for root, dirs, files in os.walk(x):
        for file in files:
            if '.md' not in file:
                continue
            fpath = os.path.join(root, file)
            rel_path = os.path.relpath(fpath, script_dir)
            print(f"processing {rel_path}")
            header = extract_yaml(fpath)
            if not header:
                print(f"{rel_path} has no header")
                continue
            title = header['title']
            if 'date' in header:
                if type(header['date']) is str:
                    date = header['date']
                else:
                    date = header['date'].strftime("%Y-%m-%d")
            else:
                date = "1900-01-01"
            output.append((title, date, rel_path.replace('.md', '.html')))
    return sorted(output, key=lambda x: x[1], reverse=True)

blog_data = '\n'.join([f"* [{t}]({p})" for t, _, p in walk_tree(blog_dir)])
project_data = walk_tree(projects_dir)
index_template = (script_dir / Path('itemplate.txt'))
index = (script_dir / Path('index.md'))
index.write_text(index_template.read_text().replace('$blog_data$', blog_data))
print('DONE')

