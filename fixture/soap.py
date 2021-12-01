from suds.client import Client
from suds import WebFault

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        lst = []
        for i in client.service.mc_projects_get_user_accessible("administrator", "root"):
            lst.append(i.name)
        return lst

