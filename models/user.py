#!/usr/bin/python3
"""Module user"""
from datetime import datetime
from models import base_model
import models


class User(base_model.BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
