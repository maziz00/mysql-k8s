from fastapi import FastAPI, Request
import mysql.connector
import os

app = FastAPI()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

@app.on_event("startup")
def startup():
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ips (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ip VARCHAR(50) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

@app.post("/log-ip")
async def log_ip(request: Request):
    client_ip = request.client.host
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ips (ip) VALUES (%s)", (client_ip,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "IP logged", "ip": client_ip}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)