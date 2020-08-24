from telethon import TelegramClient, events, errors
import json

session_file = 'telegramBot'
import configparser

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
source_group1 = json.loads(config.get("Telegram", "telegram_source_group_id1"))
target_group = config['Telegram'].getint('telegram_target_group_id')

telegramClient = TelegramClient(username, api_id, api_hash)


@telegramClient.on(events.NewMessage(source_group1, blacklist_chats=False))
async def newMessageHandler1(msg):
    await telegramClient.forward_messages(target_group, msg.id, source_group1)


try:
    telegramClient.start()
    print("-------------------------\nMessage Forward bot is up!\n-------------------------\n")
    telegramClient.run_until_disconnected()
except KeyboardInterrupt:
    print("[+] Quiting bot!")
except errors.rpcerrorlist.ApiIdInvalidError:
    print("[+] Invalid API_ID/API_HASH")
