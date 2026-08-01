from pydantic import BaseModel


class IslamicResponse(BaseModel):

    answer: str

    source: str

    topic: str