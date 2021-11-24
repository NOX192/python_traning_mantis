from model.project import Project

def test_delete_project(app):
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
    old_projects = app.projects.get_project_list()
    for o in old_projects:
        if o.name == "NewName":
            break
        index += 1
    app.projects.delete_by_project_name("NewName")
    new_projects = app.projects.get_project_list()
    del old_projects[index]
    assert sorted(str(old_projects)) == sorted(str(new_projects))