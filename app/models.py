from pydantic import BaseModel, Field
from enum import Enum

class PidorasLevel(str, Enum):
    Ancient = "Уникальнейший пидарас"
    Legendary = "Легендарный пидарас"
    Immortal = "Пидарас с выебонами"
    Epic = "Эпический пидарас"
    Mythical = "Мифический пидарас"
    Uncommon = "Необычный пидарас"
    Common = "Самый обычный пидарас"


class PidorasReason(str):
    default_reason = "сосал"


class PidorasName(str):
    default_name = "Антон"


class Pidaras(BaseModel):
    name: str = Field(default = PidorasName.default_name, description = "Имя пидараса")
    pidaras_level: PidorasLevel = Field(default = PidorasLevel.Common, description = "Редкость пидораса")
    reason: str = Field(default = PidorasReason.default_reason, description = "Причина добавления в список")
    is_dota_player: bool = Field(default = True, description = "Играет он в доту или нет")
    is_cs_player: bool = Field(default = True, description = "Играет он в кс или нет")
    


