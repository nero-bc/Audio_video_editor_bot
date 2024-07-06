import os
from utils import trim_video, remove_audio, trim_audio, merge_videos
from database import insert_video, get_video_path

async def handle_query(video_file):
    file_id = video_file.file_id

    # Perform an action (example: remove audio)
    output_path = os.path.join('processed', f'{file_id}_no_audio.mp4')
    await remove_audio(file_id, output_path)

    # Insert into database
    insert_video(file_id, output_path)

    return output_path

async def retrieve_video_path(file_id):
    return get_video_path(file_id)
