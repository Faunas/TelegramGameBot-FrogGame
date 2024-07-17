import asyncio
from telethon import TelegramClient, events
from config import api_id, api_hash, bot_token

chat_with_bot = *
user_id_to_check = *

async def send_message(client, chat_id, message):
    try:
        await client.send_message(chat_id, message)
    except Exception as e:
        print(f"Error: {e}")

async def schedule_message(interval, message, client, chat_id, repeat=True, delay=None):
    if delay:
        await asyncio.sleep(delay)
    while True:
        await send_message(client, chat_id, message)
        if not repeat:
            break
        await asyncio.sleep(interval)


# Initialize the Telegram client
client = TelegramClient('myGrab', api_id, api_hash, system_version="4.16.30-vxMAX")

async def main():
    await client.start()
    await client.connect()

    # Schedule other messages
    tasks = [
        schedule_message(6 * 60 * 60, "@toadbot Поход в столовую", client, chat_with_bot),   # Every 6 hours
        schedule_message(8 * 60 * 60, "@toadbot Завершить работу", client, chat_with_bot),  # Every 8 hours
        schedule_message(12 * 60 * 60, "@toadbot Покормить жабу", client, chat_with_bot),    # Every 12 hours
        schedule_message(8 * 60 * 60, "@toadbot Покормить жабенка", client, chat_with_bot), # Every 12 hours
        schedule_message(5 * 24 * 60 * 60, "@toadbot Брак вознаграждение", client, chat_with_bot), # Every 5 days
        schedule_message(8 * 60 * 60, "@toadbot Отправить жабенка в детсад", client, chat_with_bot), # Every 8 hours
        schedule_message(14 * 60 * 60, "@toadbot Забрать жабенка", client, chat_with_bot), # Every 14 hours
    ]

    await asyncio.gather(*tasks)

    # Keep the client running to listen for new messages
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
