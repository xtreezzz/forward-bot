import configparser
from telethon.sync import TelegramClient

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

client = TelegramClient(username, api_id, api_hash)
client.start()


async def main():
	async for dialog in client.iter_dialogs():
		print(f'{dialog.name};{dialog.id}')


with client:
	client.loop.run_until_complete(main())