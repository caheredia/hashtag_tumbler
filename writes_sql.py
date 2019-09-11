import sqlite3
import datetime
import time

conn = sqlite3.connect("hashtag.db")

c = conn.cursor()

# print initial row count
c.execute("SELECT COUNT(*) FROM hashtags")
print(c.fetchall())


def add_tag(tag):
    c.execute(
        "INSERT INTO hashtags VALUES (:user,:category,:tag)",
        {"user": "xristian", "category": "leica", "tag": tag},
    )
    conn.commit()


def save_rate(write_rate):
    """Save rates to rate table."""
    c.execute(
        "INSERT INTO rates VALUES (:method,:rate)",
        {"method": "sql", "rate": write_rate},
    )
    conn.commit()


def calculate_write_rate(rows):
    """Returns write rate to write integer number of rows."""
    start = time.time()
    for i in range(rows):
        time_now = datetime.datetime.now().isoformat()
        add_tag(time_now)
    end = time.time()
    delta = end - start
    print(f"toatl time: {delta}")
    write_rate = int(rows / delta)
    print(f"Rows/second: {write_rate}")
    return write_rate


def multiple_runs(rows, runs):
    """"Run writes multiple times and save results to rates table."""
    for i in range(runs):
        write_rate = calculate_write_rate(rows)
        save_rate(write_rate)


multiple_runs(rows=1000, runs=10)

# print final row count
c.execute("SELECT COUNT(*) FROM hashtags")
print(c.fetchall())

conn.close()

