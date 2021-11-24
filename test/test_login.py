

def test_login(app):
    app.session.login("administrator", "root")
    assert app.session.is_logget_in_as("administrator")