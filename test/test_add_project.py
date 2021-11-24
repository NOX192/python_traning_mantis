from model.project import Project

def test_add_project(app):
    if len(app.projects.get_project_list()) > 0:
        for i in app.projects.get_project_list():
            if i.name == "NewName":
                app.projects.delete_by_project_name("NewName")
    old_projects = app.projects.get_project_list()
    app.projects.create_new_project(Project(name="NewName", description="NewDescription"))
    new_projects = app.projects.get_project_list()
    old_projects.append(Project(name="NewName", description="NewDescription"))
    assert sorted(str(old_projects)) == sorted(str(new_projects))
