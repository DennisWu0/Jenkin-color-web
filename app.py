from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "demo")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")

def get_color():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cur = conn.cursor()
    cur.execute("SELECT color FROM colors ORDER BY id DESC LIMIT 1;")
    row = cur.fetchone()
    cur.close()
    conn.close()

    return row[0] if row else "white"

@app.route("/")
def index():
    color = get_color()
    return render_template("index.html", color=color)

@app.route("/health")
def health():
    return {"status": "ok"}, 200
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
