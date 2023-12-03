import os

from webexteamssdk import WebexTeamsAPI
from webexteamssdk.models.cards import Colors, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, \
    Image, ImageSize, Fact, FactSet
from webexteamssdk.models.cards.actions import OpenUrl
from webexteamssdk.models.cards.components import TextBlock

from utils import get_type_emoji, get_priority_emoji

image = Image(
    url="https://i.imgur.com/ycIQYjY.png",
    size=ImageSize.AUTO)
WEBEX_SPACE_ID = os.getenv('WEBEX_SPACE_ID')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

webex_api = WebexTeamsAPI(access_token=ACCESS_TOKEN)


def build_card(ticket):
    type = ticket.type
    priority = ticket.priority
    type_emoji = get_type_emoji(type)
    priority_emoji = get_priority_emoji(priority)

    bot_facts = [Fact(title="Type", value=f"{ticket.type} {type_emoji}"),
                 Fact(title="Priority", value=f"{ticket.priority} {priority_emoji}")
                 ]

    heading = TextBlock(ticket.key, weight=FontWeight.BOLDER, wrap=True, size=FontSize.LARGE)

    header_column = Column(items=[heading], width=2)
    header_image_column = Column(
        items=[image],
        width=1,
    )

    max_tokens_info_textblock = TextBlock(f"**Summary:** {ticket.summary}",
                                          wrap=True, size=FontSize.SMALL, color=Colors.LIGHT)

    card = AdaptiveCard(
        body=[ColumnSet(columns=[header_column, header_image_column]),
              FactSet(facts=bot_facts),
              ColumnSet(columns=[Column(items=[max_tokens_info_textblock], width=2)]),
              ], actions=[OpenUrl(url=ticket.link, title="Navigate to ticket")])
    webex_api.messages.create(text="looks like https://www.tms.netcracker.com is down", roomId=WEBEX_SPACE_ID,
                              attachments=[card])
