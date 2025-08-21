# coding: utf-8

import os

"""
APIサーバの接続設定
"""

VALID_API_SERVER_SETTINGS = {
    "host": os.environ["API_SERVER"],
    "username": os.environ["USERNAME"],
    "password": os.environ["PASSWORD"],
}
