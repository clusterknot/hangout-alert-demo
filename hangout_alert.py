from httplib2 import Http
from json import dumps

def alert(filename):
    url = "https://chat.googleapis.com/v1/spaces/AAAAMPGdQ5M/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=KFGqEGq3dpyLd9kT1MCRHe5i-FwQgkzSNizC6uS8NAA%3D"

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