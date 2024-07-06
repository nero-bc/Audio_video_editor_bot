import sqlite3

def init_db():
    conn = sqlite3.connect('bot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, chat_id INTEGER, file TEXT)''')
    conn.commit()
    conn.close()

def add_task(chat_id, file):
    conn = sqlite3.connect('bot.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (chat_id, file) VALUES (?, ?)", (chat_id, file))
    task_id = c.lastrowid
    conn.commit()
    conn.close()
    return task_id

def get_task(task_id):
    conn = sqlite3.connect('bot.db')
    c = conn.cursor()
    c.execute("SELECT file FROM tasks WHERE id=?", (task_id,))
    file = c.fetchone()
    conn.close()
    return {'file': file[0]} if file else None
