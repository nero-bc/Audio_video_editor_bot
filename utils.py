import ffmpeg
from tqdm import tqdm
import time

def trim_video(file, start_time, end_time):
    start_time_sec = convert_to_seconds(start_time)
    end_time_sec = convert_to_seconds(end_time)
    trimmed_file = "trimmed.mp4"

    input_stream = ffmpeg.input(file, ss=start_time_sec, to=end_time_sec)
    ffmpeg.output(input_stream, trimmed_file).run()
    
    return trimmed_file

def remove_audio(file):
    video = ffmpeg.input(file)
    video_no_audio_file = "no_audio.mp4"

    ffmpeg.output(video, video_no_audio_file, an=None).run()
    return video_no_audio_file

def convert_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s
