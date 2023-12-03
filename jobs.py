import os

import feedparser
import requests
from urllib3.exceptions import MaxRetryError

from cards import build_card
from models import Jira
from utils import get_priority, get_type, get_key

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
FEED_URL = os.getenv('FEED_URL')

previous_tickets = []  # declare the global variable here


def retrieve_rss():
    # create an authenticated session
    global previous_tickets  # declare 'previous_tickets' as global

    with requests.session() as session:
        session.auth = (USERNAME, PASSWORD)
        # fetch the rss feed using the authenticated session
        try:
            response = session.get(FEED_URL)
            feed = feedparser.parse(response.content)
            new_tickets = []
            for item in feed.entries:
                key = get_key(item.link)
                if key not in (p.key for p in previous_tickets):
                    priority = get_priority(item.priority['id'])
                    ticket_type = get_type(item.type['id'])
                    ticket = Jira(key, item.link, ticket_type, priority, item.summary)
                    build_card(ticket)
                    new_tickets.append(ticket)
            previous_tickets += new_tickets
        except MaxRetryError:
            pass
