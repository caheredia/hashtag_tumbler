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
    # conn.close()
    await db.close()


@app.route("/total", methods=["GET"])
async def post(request):
    conn = sqlite3.connect("hashtag.db")
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM hashtags")
    data = c.fetchall()
    conn.close()
    return text(data)


@app.route("/tag", methods=["POST"])
async def post(request):
    tag = request.json["tag"]
    conn = sqlite3.connect("hashtag.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO hashtags VALUES (:user,:category,:tag)",
        {"user": "xristian", "category": "leica", "tag": tag},
    )
    conn.commit()
    conn.close()
    return text("success")


@app.route("/async-tag", methods=["POST"])
async def post(request):
    tag = request.json["tag"]
    await db.execute(
        "INSERT INTO hashtags VALUES (:user,:category,:tag)",
        {"user": "xristian", "category": "leica", "tag": tag},
    )
    await db.commit()
    return text("success")


asyncio.set_event_loop(uvloop.new_event_loop())
server = app.create_server(host="0.0.0.0", port=8000, return_asyncio_server=True)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(server)
try:
    loop.run_forever()
except KeyboardInterrupt:
    loop.stop()
    sys.exit(0)
