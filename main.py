import requests
import time

API_URL: str = 'https://api.telegram.org/bot'
API_URL_CATS: str='https://api.thecatapi.com/v1/images/search'
BOT_TOKEN: str = '6251976390:AAGOCj5qjHwjAAka0eVxu7u5F-1wmDIQI-E'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
MAX_COUNTER: int = 1001

offset: int = -2
counter: int = 0
cat_response: requests.Response
chat_id: int

while counter < MAX_COUNTER:
    print('attempt=', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_URL_CATS)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
    time.sleep(1)
    counter += 1
