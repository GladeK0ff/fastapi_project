from pydantic import BaseModel


class PidarasAddSchema(BaseModel):
    name: str 
    pidaras_level: str
    reason: str 
    is_dota_player: bool 
    is_cs_player: bool 


class PidarasSchema(PidarasAddSchema):
    id: int