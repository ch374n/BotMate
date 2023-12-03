import logging

from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card
from webexteamssdk.models.cards import TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, \
    Image, ImageSize, ImageStyle
from webexteamssdk.models.cards.actions import Submit

log = logging.getLogger(__name__)

TRANSLATE_ICON = "https://i.imgur.com/1kvSlGE.png"


class TranslationHelp(Command):

    def __init__(self):
        super().__init__(
            command_keyword="translations_card",
            help_message="Get translations menu")

    def execute(self, message, attachment_actions, activity):
        title = TextBlock("Translations Menu", weight=FontWeight.BOLDER, wrap=True, size=FontSize.LARGE)

        image = Image(
            url=TRANSLATE_ICON,
            style=ImageStyle.PERSON,
            size=ImageSize.AUTO)

        header_column = Column(items=[title], width=2)
        header_image_column = Column(
            items=[image],
            width=1,
        )
        to_english = Submit(title="Russian text to English",
                            data={
                                "command_keyword": "en"})
        to_russian = Submit(title="English text to Russian",
                            data={
                                "command_keyword": "ru"})
        all_commands = Submit(title="List all commands",
                              data={
                                  "command_keyword": "list_all_commands"})
        card = AdaptiveCard(
            body=[ColumnSet(columns=[header_column, header_image_column]),
                  ],
            actions=[to_english, to_russian, all_commands])
        return response_from_adaptive_card(card)
