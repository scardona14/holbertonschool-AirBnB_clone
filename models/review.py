#!/usr/bin/python3

"""creates class review"""


from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
