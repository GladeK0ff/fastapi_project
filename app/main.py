from fastapi import FastAPI, HTTPException
from app.models import Pidaras
import uvicorn

app = FastAPI()
pidaras = Pidaras
pidarases_list = [
    {
        "id": 1,
        "name": "Антон",
        "pidaras_level": "MAXIMUM",
        "reason": "сосал ТАК ДОХУЯ РАЗ, что уже не говорит нет",
        "is_dota_player": "True",
        "is_cs_player": "True",
    }
]

@app.get('/')
async def get_list_pidarases():
    if len(pidarases_list) > 0:
        return pidarases_list
    return {"message": "Sorry, but the list of pidarases is empty"}


@app.get('/one_pidaras/{pidaras.id}')
async def get_one_pidaras(pid_id: int):
    for pid in pidarases_list:
        if pid["id"] == pid_id:
            return pid
    raise HTTPException (status_code=404, detail='Такого пидараса мы не знаем, но ты всегда можешь его добавить через "/inputp"')


@app.post('/inputp')
async def post_pidaras(pidaras: Pidaras):
    pidarases_list.append({
        "id": pidarases_list[-1]["id"] + 1,
        "name": pidaras.name,
        "pidaras_level": pidaras.pidaras_level,
        "reason": pidaras.reason,
        "is_dota_player": pidaras.is_dota_player,
        "is_cs_player": pidaras.is_cs_player,
    })
    return 'spasibo chto dobavili pidorasa'


@app.put('/update_pidaras/{pidaras.id}')
async def update_pidaras(pidaras: Pidaras, pid_id: int):
    for pid in pidarases_list:
        if pid["id"] == pid_id:
            pid["name"] = pidaras.name
            pid["pidaras_level"] = pidaras.pidaras_level
            pid["reason"] = pidaras.reason
            pid["is_dota_player"] = pidaras.is_dota_player
            pid["is_cs_player"] = pidaras.is_cs_player
            return {"message" "Информация о пидарасе обновлена, спасибо за бдительность"}
    raise HTTPException(status_code=404, detail='Такого пидараса мы не знаем, но ты всегда можешь его добавить через "/inputp"')

    
@app.delete('/delete_pidarasa/{pidaras.id}')
async def delete_pidoras(pid_id: int):
    for pid in pidarases_list:
        if pid["id"] == pid_id:
            pidarases_list.remove(pid)
            return f'Не знаю зачем, но Вы удалили пидараса'
    raise HTTPException(status_code=404, detail='Такого пидараса мы не знаем, но ты всегда можешь его добавить через "/inputp"')



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

     