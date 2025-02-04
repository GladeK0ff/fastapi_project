from fastapi import FastAPI, HTTPException
from models import PidarasAddSchema
import psycopg2


app = FastAPI()

pidaras = PidarasAddSchema

# Подключение к базе данных postgres
conn = psycopg2.connect(dbname="pidarases", user="postgres", password="password", host="postgres", port="5432")


cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS pidaras (
  id SERIAL PRIMARY KEY,
  pidaras_name varchar(50) not null,
  pidaras_level varchar (70),
  reason varchar (255),
  is_dota_player boolean, 
  is_cs_player boolean
);
''')

conn.commit()


@app.get("/list")
async def get_pidarases():
    cur.execute("SELECT * FROM pidaras;")
    result = cur.fetchall()
    return result


@app.post("/inputp")
async def post_pidaras(pidaras: PidarasAddSchema):
    cur.execute(f'''
                INSERT into pidaras(pidaras_name, pidaras_level, reason, is_dota_player, is_cs_player) 
                values ('{pidaras.name}', '{pidaras.pidaras_level}', '{pidaras.reason}', {pidaras.is_dota_player}, {pidaras.is_cs_player});
                ''')
    conn.commit()
    return {"msg": "плюс пидарас"}






     