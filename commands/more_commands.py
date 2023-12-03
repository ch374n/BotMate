from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card
from webexteamssdk.models.cards import TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, Colors
from webexteamssdk.models.cards.actions import ShowCard


class More(Command):

    def __init__(self):
        super().__init__(
            command_keyword="list_all_commands",
            help_message="List all commands")

    def execute(self, message, attachment_actions, activity):
        items = [TextBlock("@BotMate list_all_commands", wrap=True, color=Colors.LIGHT, size=FontSize.MEDIUM),
                 TextBlock("@BotMate en <text>", wrap=True, color=Colors.LIGHT, size=FontSize.MEDIUM),
                 TextBlock("@BotMate ru <text>", wrap=True, color=Colors.LIGHT, size=FontSize.MEDIUM),
                 TextBlock("@BotMate summarise <text>", wrap=True, color=Colors.LIGHT, size=FontSize.MEDIUM),
                 TextBlock("@BotMate tms_monitoring", wrap=True, color=Colors.LIGHT, size=FontSize.MEDIUM),
                 TextBlock("@BotMate ask <question>", wrap=True, color=Colors.LIGHT, size=FontSize.MEDIUM),
                 ]
        adaptive_card = AdaptiveCard(
            body=[ColumnSet(columns=[Column(items=items, width=2)]),
                  ])

        show_card = ShowCard(
            title="See all commands",
            card=adaptive_card
        )
        heading = TextBlock("Available Commands", weight=FontWeight.BOLDER, wrap=True, size=FontSize.SMALL)

        header_column = Column(items=[heading], width=2)
        card = AdaptiveCard(
            body=[ColumnSet(columns=[header_column])
                  ],
            actions=[show_card])
        return response_from_adaptive_card(card)
