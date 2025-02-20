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


@app.get("/one/{pid}")
async def get_one_pidaras(pid: int):
  cur.execute(f"SELECT * FROM pidaras where id = {pid};")
  result = cur.fetchall()
  if result:
    return result
  return {"msg": f'не знаем пидараса с id = {pid}'}
  


@app.get("/list")
async def get_pidarases():
  cur.execute("SELECT * FROM pidaras;")
  result = cur.fetchall()
  if result:
    return result
  return {"msg": "база пидарасов пуста... пока что"}


@app.post("/inputp")
async def post_pidaras(pidaras: PidarasAddSchema):
  cur.execute(f'''
              INSERT into pidaras(pidaras_name, pidaras_level, reason, is_dota_player, is_cs_player) 
              values ('{pidaras.name}', '{pidaras.pidaras_level}', '{pidaras.reason}', {pidaras.is_dota_player}, {pidaras.is_cs_player});
              ''')
  conn.commit()
  return {"msg": "плюс пидарас"}


@app.put("/correct/{pid}")
async def put_pidaras(pidaras: PidarasAddSchema, pid):
  cur.execute(f"SELECT * FROM pidaras where id = {pid};")
  result = cur.fetchall()
  if result:
    cur.execute(f'''UPDATE pidaras SET
                    pidaras_name = '{pidaras.name}', 
                    pidaras_level = '{pidaras.pidaras_level}', 
                    reason = '{pidaras.reason}', 
                    is_dota_player = '{pidaras.is_dota_player}', 
                    is_cs_player = '{pidaras.is_cs_player}' 
                    where id = {pid};''')
    conn.commit()
    return {"msg": "пидарас изменен"}
  return {"msg": f"не было у нас пидараса с id = {pid}"}



@app.delete("/delete/{pid}")
async def delete_pidoras(pid):
  cur.execute(f"SELECT * FROM pidaras where id = {pid};")
  result = cur.fetchall()
  if result:
    cur.execute(f"DELETE from pidaras where id = {pid}")
    conn.commit()
    return {"msg": "пидарас удален"}
  return {"msg": f"не было у нас пидараса с id = {pid}"}

    








     