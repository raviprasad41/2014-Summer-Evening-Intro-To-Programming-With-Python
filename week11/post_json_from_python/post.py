import urllib
import json

extra_data = {
    'foo': 'aaa',
    'bar': 'bbb',
}

json_params = json.dumps(extra_data)

form_data = {'api_key': '123123123', 'format': 'json', 'data-type': 'json', 'data': json_params}

params = urllib.urlencode(data)

f = urllib.urlopen("http://www.musi-cal.com/cgi-bin/query", params)

print(f.read())
