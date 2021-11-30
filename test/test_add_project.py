from model.project import Project
import re

def test_add_project(app):
    app.session.login("administrator", "root")
    if len(app.projects.get_project_list()) > 0:
        for i in app.projects.get_project_list():
            if i.name == "NewName":
                app.projects.delete_by_project_name("NewName")
    old_projects = app.soap.get_project_list("administrator", "root")
    app.projects.create_new_project(Project(name="NewName", description="NewDescription"))
    new_projects = app.soap.get_project_list("administrator", "root")
    old_projects.append(Project(name="NewName"))
    assert merge_proj(str(old_projects)) == merge_proj(str(new_projects))

def merge_proj(str):
    v = re.sub(";None", "", str)
    return sorted(v)



