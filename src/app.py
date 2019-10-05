from sanic import Sanic
from sanic.response import text, json
import aiosqlite
from src.database.blueprint import database_v1
from src.constants import DATABASE_FILE

app = Sanic(__name__)
app.blueprint(database_v1)


@app.listener("before_server_start")
async def before_start(app, loop):
    print("Starting server")
    global db
    db = await aiosqlite.connect(DATABASE_FILE)


@app.listener("after_server_stop")
async def after_stop(app, loop):
    print("Closing connection to sqlite")
    await db.close()


@app.route("/health", methods=["GET"])
async def health(request):
    return json({"database open": db.is_alive()}, status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False, access_log=False)
