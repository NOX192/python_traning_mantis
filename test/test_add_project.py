import re

def test_add_project(app):
    creating_project_name = "NewName"
    description = "NewDescription"
    app.projects.check_that_project_deleted(creating_project_name)
    old_projects = app.soap.get_project_list()
    app.projects.create_new_project(creating_project_name, description)
    new_projects = app.soap.get_project_list()
    old_projects.append(creating_project_name)
    assert merge_proj(str(old_projects)) == merge_proj(str(new_projects))

def merge_proj(str):
    v = re.sub("\'", "", str)
    return sorted(v)



