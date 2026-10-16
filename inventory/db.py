"""Saves the inventory to SQLite and searches it."""

import sqlite3


def connect(path):
    conn = sqlite3.connect(path)
    conn.execute("CREATE TABLE IF NOT EXISTS items (name TEXT, quantity INTEGER, price REAL)")
    return conn


def save_items(conn, items):
    for item in items:
        conn.execute("INSERT INTO items VALUES (?, ?, ?)", (item.name, item.quantity, item.price))
    conn.commit()


def search(conn, term):
    cur = conn.execute("SELECT * FROM items WHERE name LIKE ?", ('%' + term + '%',))
    return cur.fetchall()


def page(rows, page_number, page_size=10):
    start = page_number * page_size
    return rows[start:start + page_size + 1]


def tag_item(name, tags=None):
    if tags is None:
        tags = []
    tags.append(name)
    return tags
