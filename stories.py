from instapy_cli import client

def upload_stories(image):
    username = 'clippingcatolico'
    password = 'neto1234'
    image = image

    with client(username, password) as cli:
        cli.upload(image, story=True)