import logging

from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card
from webexteamssdk.models.cards import TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, \
    Image, ImageSize, Colors, ImageStyle
from webexteamssdk.models.cards.actions import Submit

log = logging.getLogger(__name__)

BOTMATE_ICON = "https://i.imgur.com/Gq2Ftwh.png"


class CustomHelp(Command):

    def __init__(self):
        super().__init__(
            command_keyword="help",
            help_message="Get help menu")

    def execute(self, message, attachment_actions, activity):
        bot_version_info = "BotMate here 🤙"

        subtitle = TextBlock("Help Menu", weight=FontWeight.BOLDER, wrap=True, size=FontSize.LARGE)
        heading = TextBlock(bot_version_info, wrap=True, size=FontSize.SMALL, color=Colors.LIGHT)

        image = Image(
            url=BOTMATE_ICON,
            style=ImageStyle.PERSON,
            size=ImageSize.AUTO)

        header_column = Column(items=[heading, subtitle], width=2)
        header_image_column = Column(
            items=[image],
            width=1,
        )
        monitoring = Submit(title="Monitoring 🧐",
                            data={
                                "command_keyword": "monitoring_card"})
        translation = Submit(title="Translation 🖊️",
                             data={
                                 "command_keyword": "translations_card"})
        knowledge_base = Submit(title="Knowledge base 🤓",
                                data={
                                    "command_keyword": "ask"})
        summarise = Submit(title="Summarise 📋",
                           data={
                               "command_keyword": "summarise"})
        all_commands = Submit(title="List all commands",
                              data={
                                  "command_keyword": "list_all_commands"})
        card = AdaptiveCard(
            body=[ColumnSet(columns=[header_column, header_image_column]),
                  ],
            actions=[monitoring, translation, knowledge_base, summarise, all_commands])
        return response_from_adaptive_card(card)
