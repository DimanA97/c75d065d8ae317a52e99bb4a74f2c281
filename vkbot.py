import vk_api

def captcha_handler(captcha):
    
    key = input("Enter Captcha {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)

def main():

    login, password = 
    vk_session = vk_api.VkApi(login, password, captcha_handler=captcha_handler)
    
    try:
        vk_session.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api() #most important thing!!!!!!11111
    while True:
        message = vk.messages.get(out = 0, count = 1)
        message_id = message['items'][0]['id']
        if message['items'][0]['read_state'] == 0:
            if message['items'][0]['body'] == 'Бот, помощь':
                vk.messages.send(chat_id = message['items'][0]['chat_id'], message = 'Мои команды: Бот, привет; Бот, как дела?', forward_messages = message_id)
            if message['items'][0]['body'] == 'Бот, привет':
                vk.messages.send(chat_id = message['items'][0]['chat_id'], message = "Привет", forward_messages = message_id, attachment = 'photo159872158_424286978')
            if message['items'][0]['body'] == 'Бот, как дела?':
                vk.messages.send(chat_id = message['items'][0]['chat_id'], message = "Работаю, как видишь", forward_messages = message_id)
            vk.messages.markAsRead(messages_ids = message_id, peer_id = 2000000000 + message['items'][0]['chat_id'])
            continue
            
            
            
                    


        
main()











#
#
#                           БЭКАП 1!!!!!
#
#
'''
def main():

    login, password = 
    vk_session = vk_api.VkApi(login, password, captcha_handler=captcha_handler)
    
    try:
        vk_session.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api() #most important thing!!!!!!11111
    
    message = vk.messages.get(out = 0, count = 1, last_message_id = 0)
    message_id = message['items'][0]['id']
    if message['items'][0]['body'] == 'Вэл, привет':
       send = vk.messages.send(chat_id = message['items'][0]['chat_id'], message = "Привет", forward_messages = message_id) #, attachment = 'photo159872158_424286978')
       message1 = vk.messages.get(out = 0)
       print(send)

'''

#
#
#
#               БЕКАП 2!!!!!!!!!!
#
'''
def main():

    login, password = 
    vk_session = vk_api.VkApi(login, password, captcha_handler=captcha_handler)
    
    try:
        vk_session.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api() #most important thing!!!!!!11111
    while True:
        message = vk.messages.get(out = 0, count = 1)
        message_id = message['items'][0]['id']
        if message['items'][0]['read_state'] == 0:
            if message['items'][0]['body'] == 'Бот, привет':
                vk.messages.send(chat_id = message['items'][0]['chat_id'], message = "Привет", forward_messages = message_id, attachment = 'photo159872158_424286978')
            if message['items'][0]['body'] == 'Бот, как дела?':
                vk.messages.send(chat_id = message['items'][0]['chat_id'], message = "Rabotau", forward_messages = message_id)
            vk.messages.markAsRead(messages_ids = message_id, peer_id = 2000000000 + message['items'][0]['chat_id'])
            continue

'''
