from pydantic import BaseModel


class Component(BaseModel):
    component: str
    country: str
    description: str
    model: str
