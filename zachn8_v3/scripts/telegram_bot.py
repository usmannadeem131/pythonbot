import requests
import json

############ Telegram functions Start###########

TOKEN = "6415872150:AAFgl8Q79yq6Atja9Ksj9PsI_T661kASOd4"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

headers = {"Accept": "application/json"}
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    # print (url)
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["channel_post"]["text"]
    chat_id = updates["result"][last_update]["channel_post"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=HTML".format(text, chat_id)
    get_url(url)

############ Telegram functions End###########

if __name__ == "__main__":
    # latest_message=get_last_chat_id_and_text(get_updates())
    # listlatest_message=latest_message[0].split('\n')

    # sub=re.match('Race:  (.*) ([0-9]*:[0-9]*)',listlatest_message[2]).groups() 
    # timing=sub[1] 
    # raceAt=sub[0] 
    # sub=re.match('Selection:  [0-9]*. ([a-zA-Z ]*)',listlatest_message[3])
    # hourseName=sub.group(1) 
    # sub=re.match('Best Price:  ([0-9\.]*) - [a-zA-Z ]*',listlatest_message[4])
    # odds=sub.group(1) 
    # race=json.dumps([{"raceAt": raceAt,"time":timing,"horseName":hourseName,"odds":odds}])

    # name=re.match('Race:(.*)[0-9]{2}:[0-9]*',latest_message[0]).group(1)
    # print(timing)
    # print(raceAt)
    # print(hourseName)
    # print(odds)
    # print(listlatest_message)


    #################################################
    # print(get_updates())
    telegram_message=f'<b>Category: </b>{"elements_category.text"}'
    telegram_message=telegram_message+f'<b>Location: </b>{"elements_with_location.text"}'
    telegram_message=telegram_message+f'<b>Click</b> <a href="{"https://www.facebook.com"}">Here</a>'
    print(telegram_message)
    send_message(str(telegram_message), -4091932256)
    # send_message('<h1>Hello</h1>', -4091932256)