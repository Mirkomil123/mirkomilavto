import sqlite3
from datetime import datetime
import hashlib


def connection():
    con = sqlite3.connect('dtb.db')
    return con


def create_table_user():
    con = connection()
    cursor = con.cursor()
    cursor.execute("""
        create table if not exists user(
            id integer not null primary key autoincrement,
            first_name VARCHAR(30), 
            last_name VARCHAR(30),
            email varchar(50),
            username varchar(50),
            password varchar(50),
            is_active boolean default false,
            register_date datetime
        )
    """)
    con.commit()
    con.close()


def insert_user(data: dict):
    conn = connection()
    cur = conn.cursor()
    sha256 = hashlib.sha256()
    sha256.update(data['password'].encode('utf-8'))
    hashed_password = sha256.hexdigest()
    query = """
        insert into user(
        first_name,
        last_name,
        email,
        username,
        password,
        register_date
        )
        values (?,?,?,?,?,?)
    """
    values = (
        data['first_name'], data['last_name'], data['email'], data['username'], hashed_password, data[datetime.now()])
    cur.execute(query, values)
    conn.commit()
    conn.close()
