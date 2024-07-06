import os
import sqlite3
import subprocess
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils import trim_video, remove_audio, trim_audio, merge_videos
from query import handle_query
from config import API_ID, API_HASH, BOT_TOKEN

# Initialize Pyrogram client
app = Client("video_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Connect to SQLite database
conn = sqlite3.connect('videos.db')
c = conn.cursor()

# Create videos table if it does not exist
c.execute('''CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY AUTOINCREMENT, file_id TEXT, file_path TEXT)''')
conn.commit()

# Define bot commands and message handlers
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Hello! I am a video processing bot. Send me a video file to get started.")

@app.on_message(filters.video | filters.document)
async def handle_video(client, message):
    video_file = message.video or message.document

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Trim Video", callback_data=f"trim_video:{video_file.file_id}")],
        [InlineKeyboardButton("Remove Audio", callback_data=f"remove_audio:{video_file.file_id}")],
        [InlineKeyboardButton("Trim Audio", callback_data=f"trim_audio:{video_file.file_id}")],
        [InlineKeyboardButton("Merge Videos", callback_data=f"merge_videos:{video_file.file_id}")]
    ])
    
    await message.reply_text("Choose an action:", reply_markup=keyboard)

# Handle inline keyboard button actions
@app.on_callback_query()
async def callback_query(client, callback_query):
    data = callback_query.data
    action, file_id = data.split(":")
    
    if action == "trim_video":
        # Example for trimming video
        output_path = f"processed/{file_id}_trimmed.mp4"
        await trim_video(file_id, "00:00:10", "00:00:20", output_path)
        await callback_query.message.reply_document(output_path)
    
    elif action == "remove_audio":
        output_path = f"processed/{file_id}_no_audio.mp4"
        await remove_audio(file_id, output_path)
        await callback_query.message.reply_document(output_path)
    
    # Handle other actions similarly
    await callback_query.answer()

if __name__ == "__main__":
    try:
        app.run()
    except Exception as e:
        print(f"Exception occurred: {e}")
