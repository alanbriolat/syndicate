import requests


def fetch(url, filename, log=None):
    """Fetch the contents of *url* into *filename*.

    Calls *log* with a message if supplied."""
    response = requests.get(url)
    response.raise_for_status()
    f = open(filename, 'w')
    f.write(response.content)
    f.close()
    if log:
        log('Fetched %s into %s' % (url, filename))
