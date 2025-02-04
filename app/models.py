from pydantic import BaseModel


class PidarasAddSchema(BaseModel):
    name: str 
    pidaras_level: str
    reason: str 
    is_dota_player: bool 
    is_cs_player: bool 
    
    model_config ={
        "json_schema_extra":{
            "examples":[
                {
                    "name": "Антон",
                    "pidaras_level": "Common",
                    "reason": "Сосал", 
                    "is_dota_player": True,
                    "is_cs_player": True,
                }
            ]
        }
    }