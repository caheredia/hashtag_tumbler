import sqlite3
import datetime
import time

conn = sqlite3.connect("hashtag.db")

c = conn.cursor()


def add_tag(tag):
    c.execute(
        "INSERT INTO hashtags VALUES (:user,:category,:tag)",
        {"user": "xristian", "category": "leica", "tag": tag},
    )
    conn.commit()


time_now = datetime.datetime.now().isoformat()


start = time.time()
row = 1000
for i in range(row):
    add_tag(time_now)
# conn.commit()
end = time.time()
delta = end - start
print(f"toatl time: {delta}")
write_rate = int(row / delta)
print(f"Rows/second: {write_rate}")

c.execute("SELECT COUNT(*) FROM hashtags")
print(c.fetchall())

conn.close()

