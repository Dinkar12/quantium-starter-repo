import dash
from dash.testing.application_runners import import_app
from dash.testing.browser import Browser


def test_header_present():
    # Load the app
    app = import_app("app.py")

    # Start the app in a browser
    with Browser(app) as browser:
        # Assert that the header is present
        assert browser.find_element('h1')
