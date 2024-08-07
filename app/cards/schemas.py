from datetime import date

from pydantic import BaseModel


# class Labels(Enum):
#     High = 'High'
#     Middle = 'Middle'
#     Low = 'Low'


class SCards(BaseModel):
    title: str
    list_id: int
    description: str
    date_added: date
    labels: str
    deadline: date

