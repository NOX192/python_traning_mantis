from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//a[@href="/mantisbt-1.2.20/manage_overview_page.php"]').click()
        wd.find_element_by_xpath('//a[@href="/mantisbt-1.2.20/manage_proj_page.php"]').click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create_new_project(self, name, description):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_xpath("//form[@method='post']//input[@value='Create New Project']").click()
        self.change_field_value("name", name)
        self.change_field_value("description", description)
        wd.find_element_by_xpath("//form[@method='post']//input[@value='Add Project']").click()
        self.project_cache = None

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_projects_page()
            self.project_cache = []
            n = 1
            for element in wd.find_elements_by_xpath("/html/body/table[3]/tbody//tr"):
                if n > 2:
                    name = element.find_element_by_xpath(f"//tbody/tr[{n}]/td[1]/a").text
                    description = element.find_element_by_xpath(f"//tbody/tr[{n}]/td[5]").text
                    self.project_cache.append(Project(name=name, description=description))
                n += 1
        return list(self.project_cache)

    def delete_by_project_name(self, name):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_xpath(f"//a[contains(text(), '{name}')]").click()
        wd.find_element_by_xpath("//form[@method='post']//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//form[@method='post']//input[@value='Delete Project']").click()
        self.project_cache = None

    def check_contact_created(self, name, description):
        NewName_created = False
        if len(self.get_project_list()) < 1:
            self.create_new_project(name, description)
        elif len(self.get_project_list()) > 0:
            for i in self.get_project_list():
                if i.name == f"{name}":
                    NewName_created = True
                    break
            if NewName_created == False:
                self.create_new_project(name, description)

    def take_index_from_projects_list(self, projects_list, name):
        index = 0
        for o in projects_list:
            if o == f"{name}":
                break
            index += 1
        return index

    def check_that_project_deleted(self, name):
        if len(self.get_project_list()) > 0:
            for i in self.get_project_list():
                if i.name == f"{name}":
                    self.delete_by_project_name(f"{name}")