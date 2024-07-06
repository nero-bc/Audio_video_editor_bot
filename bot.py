import os
import asyncio
from pyrogram import Client, filters
from utils import trim_video, remove_audio
from query import add_task, get_task
import config

app = Client("my_bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

@app.on_message(filters.command("start"))
async def send_welcome(client, message):
    await message.reply_text("Welcome to the Video Trimmer and Audio Remover Bot!")

@app.on_message(filters.video)
async def handle_video(client, message):
    file_id = message.video.file_id
    file_path = await client.download_media(file_id)
    
    task_id = add_task(message.chat.id, file_path)
    await message.reply_text(f"Video received! Your task ID is {task_id}.")

@app.on_message(filters.command("trim"))
async def trim(client, message):
    task_id, start_time, end_time = message.text.split()[1:3]
    video_data = get_task(task_id)
    
    if video_data:
        trimmed_video = trim_video(video_data['file'], start_time, end_time)
        await client.send_video(message.chat.id, trimmed_video)
    else:
        await message.reply_text("Task ID not found!")

@app.on_message(filters.command("remove_audio"))
async def remove_audio_command(client, message):
    task_id = message.text.split()[1]
    video_data = get_task(task_id)
    
    if video_data:
        video_without_audio = remove_audio(video_data['file'])
        await client.send_video(message.chat.id, video_without_audio)
    else:
        await message.reply_text("Task ID not found!")

if __name__ == "__main__":
    app.run()
