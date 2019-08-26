import os
import shutil
import jinja2
import yaml

base_path = os.path.dirname(__file__)

projects_folder_path = os.path.join(base_path, "projects")
templates_folder_path = os.path.join(base_path, "templates")

build_folder_path = os.path.join(base_path, "build")
build_projects_folder_path = os.path.join(build_folder_path, "projects")

def get_file_content(file_path, value_if_missing=""):
    s = value_if_missing
    if os.path.exists(file_path):
        with open(file_path) as f:
            s = f.read()
    return s


class Project:
    def __init__(self, path, icon_file_name="icon.png", comment_file_name="details.txt", img_folder_name="img"):
        self.name = os.path.basename(path)

        self.path = path
        self.icon_path = os.path.join(self.path, icon_file_name)
        self.img_folder_path = os.path.join(self.path, img_folder_name)

        self.build_path = os.path.join(build_projects_folder_path, self.name)
        self.build_icon_path = os.path.join(self.build_path, icon_file_name)
        self.build_img_folder_path = os.path.join(self.build_path, img_folder_name)

        self.img_names = list(os.listdir(self.img_folder_path))
        self.comment = get_file_content(os.path.join(self.path, comment_file_name))


def clean_build_folder():
    if os.path.exists(build_folder_path):
        shutil.rmtree(build_folder_path)
    os.makedirs(build_folder_path)
    print("cleaned build folder")

def get_projects():
    if not os.path.exists(projects_folder_path):
        os.makedirs(projects_folder_path)
    return [Project(os.path.join(projects_folder_path, folder_name)) for folder_name in os.listdir(projects_folder_path)]

def get_infos():
    return yaml.safe_load(get_file_content(os.path.join(base_path, "infos.txt"), "title: ''"))

def create_jinja_env():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(templates_folder_path))
    return env

def make_index(index_template, projects, infos):
    cv = get_file_content(os.path.join(base_path, "cv.txt")) 
    rendered = index_template.render(projects=projects, cv=cv, **infos)
    index_path = os.path.join(build_folder_path, "index.html")
    with open(index_path, "w") as f:
        f.write(rendered)
    print(f"rendered {index_path}")

def make_projects(project_template, projects, infos):
    build_projects_folder_path = os.path.join(build_folder_path, "projects")

    if os.path.exists(build_projects_folder_path):
        shutil.rmtree(build_projects_folder_path)
    os.makedirs(build_projects_folder_path)

    for project in projects:
        s = project_template.render(project=project, **infos)
        os.makedirs(project.build_path)
        with open(os.path.join(project.build_path, "project.html"), "w") as f:
            f.write(s)
        shutil.copytree(project.img_folder_path, project.build_img_folder_path)
        shutil.copy2(project.icon_path, project.build_icon_path)
        print(f"built project { project.name }")
    
def copy_statics():
    shutil.copy2(os.path.join(base_path, "style.css"),
                 os.path.join(build_folder_path, "style.css"))
    print("copied statics")

def generate():
    clean_build_folder()

    env = create_jinja_env()
    projects = get_projects()
    infos = get_infos()

    copy_statics()
    make_index(env.get_template("index.html"), projects, infos)
    make_projects(env.get_template("project.html"), projects, infos)

if __name__ == "__main__":
    generate()

