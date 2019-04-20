import os
import shutil
import jinja2

base_path = os.path.dirname(__file__)
projects_folder_path = os.path.join(base_path, "projects")
templates_folder_path = os.path.join(base_path, "templates")

build_folder_path = os.path.join(base_path, "build")

class Project:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.img_names = list(os.listdir(os.path.join(path,"img")))
        self.comment = "Details du projet"

def clean_build_folder():
    if os.path.exists(build_folder_path):
        shutil.rmtree(build_folder_path)
    os.makedirs(build_folder_path)
    print("cleaned build folder")

def get_projects():
    if not os.path.exists(projects_folder_path):
        os.makedirs(projects_folder_path)
    return [Project(os.path.join(projects_folder_path, folder_name)) for folder_name in os.listdir(projects_folder_path)]

def create_jinja_env():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(templates_folder_path))
    return env

def make_index(index_template, projects):
    s = index_template.render(projects=projects)
    index_path = os.path.join(build_folder_path, "index.html")
    with open(index_path, "w") as f:
        f.write(s)
    print(f"rendered {index_path}")

def make_projects(project_template, projects):
    build_projects_folder_path = os.path.join(build_folder_path, "projects")

    if os.path.exists(build_projects_folder_path):
        shutil.rmtree(build_projects_folder_path)
    os.makedirs(build_projects_folder_path)

    for project in projects:
        s = project_template.render(project=project)
        src_path = os.path.join(projects_folder_path, project.name)
        out_path = os.path.join(build_projects_folder_path, project.name)
        os.makedirs(out_path)
        with open(os.path.join(out_path, "project.html"), "w") as f:
            f.write(s)
        shutil.copytree(os.path.join(src_path, "img"),
                        os.path.join(out_path, "img"))
        shutil.copy2(os.path.join(src_path, "icon.jpg"),
                     os.path.join(out_path, "icon.jpg"))
        print(f"built project { project.name }")
    

def copy_statics():
    shutil.copy2(os.path.join(base_path, "style.css"),
                 os.path.join(build_folder_path, "style.css"))
    print("copied statics")

def generate():
    clean_build_folder()

    env = create_jinja_env()
    projects = get_projects()

    copy_statics()
    make_index(env.get_template("index.html"), projects)
    make_projects(env.get_template("project.html"), projects)

if __name__ == "__main__":
    generate()

