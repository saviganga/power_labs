import datetime
import os
from pickle import NONE
from django.utils import timezone
import jwt
import random
import string
from xauth import models as xauth_models
from xuser import models as user_models
from xauth import exceptions as xauth_exceptions
from xauth import models as xauth_models


def find_user(username=None):# -> user_models.CustomUser:
    """
    [Find user by username]
    """
    if username == None:
        raise xauth_exceptions.UserNotFound
    try:
        user = user_models.CustomUser.objects.get(user_name=username)
        return user
    except:
        raise xauth_exceptions.UserNotFound


def encode_jwt(user, platform="API"):
    """
    Generates Auth Token
    :return: string
    """
    token = xauth_models.AuthToken.objects.create(
        token="".join(random.choice(string.ascii_letters) for i in range(7)),
        user_id=user.id,
        platform=platform,
        expiry_date = timezone.now() + datetime.timedelta(hours=72)
    )
    payload = {
        "exp": timezone.now() + datetime.timedelta(hours=72),
        "iat": timezone.now(),
        "sub": str(user.id),
        "token": token.token,
        "platform": platform
    }
    return jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm="HS256")

def regenerate_jwt(user, hours,  platform, token):
    """
    Re-generates Auth Token
    :return: string
    """
    payload = {
        "exp": timezone.now() + datetime.timedelta(hours=hours),
        "iat": timezone.now(),
        "sub": str(user.id),
        "token":token,
        "platform": platform
    }
    return jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm="HS256")

def decode_jwt(jwt_token) -> dict:
    """
    Validates the auth token and return encoded payload
    :param auth_token:
    :return: bool|dict
    """
    try:
        payload = jwt.decode(
            jwt_token, os.environ.get('SECRET_KEY'), algorithms="HS256")
        auth_token = xauth_models.AuthToken.objects.filter(
            token=payload["token"])
        if not auth_token.exists():
            raise xauth_exceptions.InvalidJwtToken
        else:
            return True, (payload, auth_token.first().user)
    except:
        return False, xauth_exceptions.InvalidJwtToken


def destroy_jwt(jwt_token: str, all=False):
    """
    Validate jwt token and delete token from the database
    :param jwt_token: str
    :param all: bool
    """
    payload, user = decode_jwt(jwt_token)
    token = payload["token"]
    if all:
        xauth_models.AuthToken.objects.filter(user_id=payload["sub"]).delete()
    else:
        xauth_models.AuthToken.objects.filter(token=token).delete()
