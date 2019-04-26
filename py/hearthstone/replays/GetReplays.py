import requests
import json
name = 'sessionid'
<<<<<<< HEAD
sessionid = '<session_id>'
=======
sessionid = '5zfk6k2wak351vhitl63m33rxggavfwc'
>>>>>>> master

cookie = {
        'version': 0,
        'name': name,
        'value': sessionid,
        'port': None,
        'domain': '',
        'path': '/',
        'secure': False,
        'expires': None,
        'discard': True,
        'comment': None,
        'comment_url': None,
        'rest': {'HttpOnly': None},
        'rfc2109': False,
    }

s = requests.session()
s.cookies.set(**cookie)

url = 'https://hsreplay.net/api/v1/games/?username=leftember%231665'
index = 0

while(True):
    response = s.get(url)
    data = response.json()
    print(f"Total: {data['count']}")
    with open(f'./r{index}.json', 'w') as fp:
        json.dump(data['results'],fp)
    url = data['next']
    if(url is None):
        break
    index = index + 1