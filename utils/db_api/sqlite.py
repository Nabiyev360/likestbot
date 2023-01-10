import sqlite3

path_to_db = 'data/main.db'


def create_table():
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS posts (
            language text,
            file_id text,
            unique_id text,
            caption text,
            likes_count integer,
            liked_users text,
            post_link text
        )""")

    conn.commit()
    conn.close()


def add_post(post_lang, file_id, unique_id, caption, likes_count=0, liked_users='', post_link=None):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    new_data = (post_lang, file_id, unique_id, caption, likes_count, liked_users, post_link)
    c.execute(f"INSERT INTO posts VALUES (?,?,?,?,?,?,?)", new_data)
    conn.commit()
    conn.close()


def add_post_link(unique_id, post_link):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"UPDATE posts SET post_link = '{post_link}' WHERE unique_id = '{unique_id}'")
    conn.commit()
    conn.close()


def get_language(unique_id):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"SELECT language FROM posts WHERE unique_id = '{unique_id}'")
    return c.fetchone()[0]


def get_post(unique_id):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"SELECT * FROM posts WHERE unique_id = '{unique_id}'")
    return c.fetchone()


def uplike(unique_id, user_id):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()

    c.execute(f"SELECT * FROM posts WHERE unique_id = '{unique_id}'")
    likes_count = c.fetchone()[4]
    c.execute(f"UPDATE posts SET likes_count = '{likes_count + 1}' WHERE unique_id = '{unique_id}'")

    c.execute(f"SELECT * FROM posts WHERE unique_id = '{unique_id}'")
    liked_users = c.fetchone()[5]

    c.execute(f"UPDATE posts SET liked_users = '{liked_users + str(user_id) + ', '}' WHERE unique_id = '{unique_id}'")
    conn.commit()
    conn.close()


def set_language(user_id, lang):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"UPDATE botUsers SET language = '{lang}' WHERE user_id = '{user_id}'")
    conn.commit()
    conn.close()


def add_channel(user_id, channel_id):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"UPDATE botUsers SET channels = '{channel_id}' WHERE user_id = '{user_id}'")
    conn.commit()
    conn.close()


def get_channel_id(user_id):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"SELECT * FROM botUsers WHERE user_id = '{user_id}'")
    return c.fetchone()[4]
