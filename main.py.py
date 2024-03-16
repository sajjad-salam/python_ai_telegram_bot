import requests
import telebot

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('6840053832:AAF17AOSNpOrcFcYnwIlsSW26pm1Mcz5zpM')




@bot.message_handler(func=lambda message: True)
def echo_all(message):
    write=message.text
    
    cookies = {
        'sessionId': '532a9edf-9a0c-436f-bc95-816b9c018aa0',
        'personalId': '532a9edf-9a0c-436f-bc95-816b9c018aa0',
        'intercom-id-jlmqxicb': '9ef873f7-0d91-4ebe-b780-6bf191ae1225',
        'intercom-session-jlmqxicb': '',
        'intercom-device-id-jlmqxicb': '65c097fd-92c8-4f8a-a616-b61f0bca56f9',
    }

    headers = {
        'authority': 'www.blackbox.ai',
        'accept': '*/*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.blackbox.ai',
        'referer': 'https://www.blackbox.ai/chat/expert-python',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'messages': [
            {
                'id': 'nBIE0Fj',
                'content': write,
                'role': 'user',
            },
           
            {
                'id': 'vVxG5kU',
                'content': 'create bots Talking by python',
                'role': 'user',
            },
        ],
        'previewToken': None,
        'userId': '582ebdf4-4ccb-4344-bffd-cfa9cf29429c',
        'codeModelMode': True,
        'agentMode': {},
        'trendingAgentMode': {
            'mode': True,
            'id': 'python',
        },
        'isMicMode': False,
        'isChromeExt': False,
        'githubToken': None,
    }

    response = requests.post('https://www.blackbox.ai/api/chat', cookies=cookies, headers=headers, json=json_data).text
    bot.reply_to(message, response)
    print(response)

bot.polling()

