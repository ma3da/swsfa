import os
import shutil

base_path = os.path.dirname(__file__)
projects_folder_path = os.path.join(base_path, "projects")

build_folder_path = os.path.join(base_path, "build")

class Project:
    def __init__(self, path):
        self.name = os.path.dirname(path)
        self.path = path
        self.img_names = [img_name for img_name in os.listdir(self.path)]
        self.detail = "Details du projet"

def get_projects():
    return [Project(os.path.join(projects_folder_path, folder_name)) for folder_name in
os.listdir(projects_folder_path)]

def copy_statics():
    pass

def copy_html():
    pass

def make_projects():
    pass

def generate():
    if os.path.exists(build_folder_path):
        shutil.rmtree(build_folder_path)
    os.makedirs(build_folder_path)
    copy_statics()
    copy_html()
    make_projects()

if __name__ == "__main__":
    generate()
