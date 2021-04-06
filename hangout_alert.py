from httplib2 import Http
from json import dumps

def alert(filename):
    url = ""

    lines = ''
    with open(filename) as file_in:
        for line in file_in:
            lines = lines + line

    chat = lines

    bot_message = {
    'text' : chat}
    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
    uri=url,
    method='POST',
    headers=message_headers,
    body=dumps(bot_message),
    )
    return 'Success'
