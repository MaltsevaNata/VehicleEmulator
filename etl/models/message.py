from pydantic import BaseModel, validator


class Message(BaseModel):
    component: str
    country: str
    description: str
    model: str

    class Config:
        validate_assignment = True

    @validator("country")
    def set_country(cls, country):
        return country or "USA"
