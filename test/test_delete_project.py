

def test_delete_project(app):
    del_project_name = "NewName"
    description = "NewDescription"
    app.projects.check_contact_created(del_project_name, description)
    old_projects = app.soap.get_project_list()
    app.projects.take_index_from_projects_list(old_projects, del_project_name)
    app.projects.delete_by_project_name(del_project_name)
    new_projects = app.soap.get_project_list()
    index = app.projects.take_index_from_projects_list(old_projects, del_project_name)
    del old_projects[index]
    assert sorted(old_projects) == sorted(new_projects)