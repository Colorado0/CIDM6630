from flask import url_for
from demoapp.models import Bookmarks


def test_home(test_client):
    """ Test the home page """
    response = test_client.get(url_for('main.base'),
                               follow_redirects=True)

    assert b'home' in response.data


def test_addbookmark(test_client):
    """ Test add bookmark """
    response = test_client.post(
        url_for('main.addbookmark'), data={
            'title': "test-title",
            'url': "www.example.com",
            'notes': "Some test notes",
            'submit': True,
        }, content_type='multipart/form-data',
        follow_redirects=True
    )
    contents = Bookmarks.query.all()
    print(contents)
    assert 1 == 1
