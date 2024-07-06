from database import add_task as db_add_task, get_task as db_get_task

def add_task(chat_id, file):
    return db_add_task(chat_id, file)

def get_task(task_id):
    return db_get_task(task_id)
