from datetime import timedelta
from enum.enums import Enum


class Timezone(Enum):
    utc = "utc"
    brt = "brt"

    @classmethod
    def toUtc(cls, referenceDatetime, timezone):
        return {
            cls.utc: referenceDatetime,
            cls.brt: referenceDatetime + timedelta(hours=3),
        }[timezone]
