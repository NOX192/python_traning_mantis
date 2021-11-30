from model.project import Project

def test_delete_project(app):
    app.session.login("administrator", "root")
    NewName_created = False
    index = 0
    if len(app.projects.get_project_list()) < 1:
        app.projects.create_new_project(Project(name="name", description="NewDescription"))
    elif len(app.projects.get_project_list()) > 0:
        for i in app.projects.get_project_list():
            if i.name == "NewName":
                NewName_created = True
                break
        if NewName_created == False:
            app.projects.create_new_project(Project(name="NewName", description="NewDescription"))
    old_projects = app.soap.get_project_list("administrator", "root")
    for o in old_projects:
        if o == "NewName":
            break
        index += 1
    app.projects.delete_by_project_name("NewName")
    new_projects = app.soap.get_project_list("administrator", "root")
    del old_projects[index]
    assert sorted(old_projects) == sorted(new_projects)