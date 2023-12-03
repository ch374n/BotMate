import os

import requests

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_URL_EN = os.getenv("API_URL_EN")
API_URL_RU = os.getenv("API_URL_RU")
API_URL_SUMMARISE = os.getenv("API_URL_SUMMARISE")
API_URL_ASK = os.getenv("API_URL_ASK")

headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}


def query_en(payload):
    response = requests.post(API_URL_EN, headers=headers, json=payload)
    return response.json()


def query_ru(payload):
    response = requests.post(API_URL_RU, headers=headers, json=payload)
    return response.json()


def query_summarise(payload):
    response = requests.post(API_URL_SUMMARISE, headers=headers, json=payload)
    return response.json()


def query_ask(payload):
    response = requests.post(API_URL_ASK, headers=headers, json=payload)
    return response.json()
