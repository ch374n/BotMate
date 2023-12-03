import logging

from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card
from webexteamssdk.models.cards import TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, \
    Image, ImageSize, ImageStyle
from webexteamssdk.models.cards.actions import Submit

log = logging.getLogger(__name__)

MONITORING_ICON = "https://i.imgur.com/l99A0ac.png"


class MonitoringHelp(Command):

    def __init__(self):
        super().__init__(
            command_keyword="monitoring_card",
            help_message="Get monitoring menu")

    def execute(self, message, attachment_actions, activity):
        title = TextBlock("Monitoring Menu", weight=FontWeight.BOLDER, wrap=True, size=FontSize.LARGE)

        image = Image(
            url=MONITORING_ICON,
            style=ImageStyle.PERSON,
            size=ImageSize.AUTO)

        header_column = Column(items=[title], width=2)
        header_image_column = Column(
            items=[image],
            width=1,
        )
        tms_monitoring = Submit(title="TMS Monitoring",
                                data={
                                    "command_keyword": "tms_monitoring"})
        kubernetes_monitoring = Submit(title="Kubernetes Monitoring",
                                       data={
                                           "command_keyword": "cluster_monitoring"})
        all_commands = Submit(title="List all commands",
                              data={
                                  "command_keyword": "list_all_commands"})
        card = AdaptiveCard(
            body=[ColumnSet(columns=[header_column, header_image_column]),
                  ],
            actions=[tms_monitoring, kubernetes_monitoring, all_commands])
        return response_from_adaptive_card(card)
