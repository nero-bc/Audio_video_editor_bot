import sqlite3

def create_connection():
    return sqlite3.connect('videos.db')

def insert_video(file_id, file_path):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO videos (file_id, file_path) VALUES (?, ?)", (file_id, file_path))
    conn.commit()
    conn.close()

def get_video_path(file_id):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT file_path FROM videos WHERE file_id=?", (file_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None
