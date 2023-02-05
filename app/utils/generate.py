from datetime import date, datetime
import jwt
from datetime import timedelta
import random
from ..settings import *


def get_token(obj):
    obj["exp"] = datetime.now() + timedelta(5)
    encoded_jwt = jwt.encode(obj,SECRET_KEY, algorithms="HS256")
    return encoded_jwt

def get_token_with_exp(obj,days,hours):
    obj["exp"] = datetime.now() + timedelta(days=days,hours=hours)
    encoded_jwt = jwt.encode(obj,SECRET_KEY, algorithm="HS256")
    return encoded_jwt


def decode_token(token):

    data = jwt. decode(token,key= SECRET_KEY, algorithms=["HS256"])
    #print(data)
    return data

def random_username(name):
    num = random.randint(1, 100)
    name=name+str(num)
    return name


def random_otp():
    otp=""
    for i in range(6):
        otp+=str(random.randint(1,9))
    return otp
