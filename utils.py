import os
import subprocess
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("video_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def download_file(file_id, output_path):
    async with app:
        file = await app.download_media(file_id, file_name=output_path)
    return file

async def trim_video(file_id, start_time, duration, output_path):
    input_path = await download_file(file_id, f"downloads/{file_id}.mp4")
    command = [
        'ffmpeg', '-i', input_path, '-ss', start_time, '-t', duration,
        '-c', 'copy', output_path
    ]
    subprocess.run(command)

async def remove_audio(file_id, output_path):
    input_path = await download_file(file_id, f"downloads/{file_id}.mp4")
    command = [
        'ffmpeg', '-i', input_path, '-an', output_path
    ]
    subprocess.run(command)

async def trim_audio(file_id, start_time, duration, output_path):
    input_path = await download_file(file_id, f"downloads/{file_id}.mp4")
    command = [
        'ffmpeg', '-i', input_path, '-ss', start_time, '-t', duration,
        '-c', 'copy', output_path
    ]
    subprocess.run(command)

async def merge_videos(video_list, output_path):
    with open('videos.txt', 'w') as f:
        for video in video_list:
            f.write(f"file '{video}'\n")
    command = [
        'ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'videos.txt', '-c', 'copy', output_path
    ]
    subprocess.run(command)
    os.remove('videos.txt')
