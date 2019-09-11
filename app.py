from sanic import Sanic
from sanic.response import text
import sqlite3
import aiosqlite
from signal import signal, SIGINT
import asyncio
import uvloop
import sys


app = Sanic(__name__)


@app.listener("before_server_start")
async def before_start(app, loop):
    print("SERVER STARTING")
    global db
    db = await aiosqlite.connect("hashtag.db")


@app.listener("after_server_stop")
async def after_stop(app, loop):
    print("Closing connection to sqlite")
    await db.close()


@app.route("/total", methods=["GET"])
async def post(request):
    cursor = await db.execute("SELECT COUNT(*) FROM hashtags")
    rows = await cursor.fetchall()
    await cursor.close()
    return text(rows)


@app.route("/tag", methods=["POST"])
async def post(request):
    tag = request.json["tag"]
    await db.execute(
        "INSERT INTO hashtags VALUES (:user,:category,:tag)",
        {"user": "xristian", "category": "leica", "tag": tag},
    )
    await db.commit()
    return text("success")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
