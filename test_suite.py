import pytest
from dash import html
from dash.testing import DashHtmlComponents


def test_header_present():
    app = DashHtmlComponents()
    app.layout = html.Div()
    with app.app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"<h1>Header</h1>" in response.data


def test_visualisation_present():
    app = DashHtmlComponents()
    app.layout = html.Div()
    with app.app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b'<div id="visualization"></div>' in response.data


def test_region_picker_present():
    app = DashHtmlComponents()
    app.layout = html.Div()
    with app.app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b'<select id="region-picker"></select>' in response.data


@pytest.mark.dash
def test_header_present():
    ...


@pytest.mark.dash
def test_visualisation_present():
    ...


@pytest.mark.dash
def test_region_picker_present():
    ...
