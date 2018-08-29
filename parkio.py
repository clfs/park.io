import requests
import typing as t

URL = 'https://park.io/domains/index/all.json'
LIMIT = 10000


def names(limit: int = LIMIT) -> t.List[str]:
    """Grab all available names."""
    r = requests.get(URL, params={'limit': limit})
    return [domain['name'] for domain in r.json()['domains']]
