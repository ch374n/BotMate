import logging

from webex_bot.formatting import quote_info
from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card
from webexteamssdk.models.cards import TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, \
    Fact, FactSet, Image, ImageSize, Colors
from webexteamssdk.models.cards.actions import OpenUrl

log = logging.getLogger(__name__)

OPENAI_ICON = "https://i.imgur.com/YChsydF.png"
CARD_CALLBACK_MORE_INFO = "help"

ENGINE = "http://rmi2.netcracker.cloud"
TEMPERATURE = 10
MAX_TOKENS = 1024


class ClusterInfo(Command):

    def __init__(self):
        super().__init__(
            command_keyword="cluster_info",
            help_message="Get cluster info",
            chained_commands=[ClusterInfoCallback()])

    #     def pre_execute(self, message, attachment_actions, activity):
    #         """
    #         (optional function).
    #         Reply before running the execute function.
    #
    #         Useful to indicate the bot is handling it if it is a long running task.
    #
    #         :return: a string or Response object (or a list of either). Use Response if you want to return another card.
    #         """
    #
    #         image = Image(url="https://i.postimg.cc/2jMv5kqt/AS89975.jpg")
    #         text1 = TextBlock("Working on it....", weight=FontWeight.BOLDER, wrap=True, size=FontSize.DEFAULT,
    #                           horizontalAlignment=HorizontalAlignment.CENTER, color=Colors.DARK)
    #         text2 = TextBlock("I am busy working on your request. Please continue to look busy while I do your work.",
    #                           wrap=True, color=Colors.DARK)
    #         card = AdaptiveCard(
    #             body=[ColumnSet(columns=[Column(items=[image], width=2)]),
    #                   ColumnSet(columns=[Column(items=[text1, text2])]),
    #                   ])
    #
    #         return response_from_adaptive_card(card)

    def execute(self, message, attachment_actions, activity):
        # text1 = TextBlock("Echo", weight=FontWeight.BOLDER, size=FontSize.MEDIUM)
        # text2 = TextBlock("Type in something here and it will be echo'd back to you. How useful is that!",
        #                   wrap=True, isSubtle=True)
        # input_text = Text(id="message_typed", placeholder="Type something here", maxLength=30)
        # input_column = Column(items=[input_text], width=2)
        #
        # submit = Submit(TITLE="Submit",
        #                 data={
        #                     "callback_keyword": "echo_callback"})
        # tb = TextBlock("This is show card", wrap=True, isSubtle=True)
        # adaptive_card = AdaptiveCard(
        #     body=[ColumnSet(columns=[Column(items=[tb], width=2)]),
        #           ])
        #
        # show_card = ShowCard(
        #     title="Show Card",
        #     card=adaptive_card
        # )
        #
        # card = AdaptiveCard(
        #     body=[ColumnSet(columns=[Column(items=[text1, text2], width=2)]),
        #           ColumnSet(columns=[input_column]),
        #           ], actions=[submit, show_card])

        bot_version_info = "Some info about me 🤙"

        bot_facts = [Fact(title="CLUSTER NAME", value=ENGINE),
                     Fact(title="TOTAL NAMESPACES", value=str(MAX_TOKENS)),
                     Fact(title="TOTAL PODS", value=str(TEMPERATURE))]

        heading = TextBlock("Cluster Info", weight=FontWeight.BOLDER, wrap=True, size=FontSize.LARGE)
        subtitle = TextBlock(bot_version_info, wrap=True, size=FontSize.SMALL, color=Colors.LIGHT)

        image = Image(
            url=OPENAI_ICON,
            size=ImageSize.AUTO)

        header_column = Column(items=[heading, subtitle], width=2)
        header_image_column = Column(
            items=[image],
            width=1,
        )

        max_tokens_info_textblock = TextBlock(
            "**Persistent Volume:** Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium "
            "doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi "
            "architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur "
            "aut odit aut fugit.",
            wrap=True, size=FontSize.SMALL, color=Colors.LIGHT)

        temp_info = "**Total Payload:** _(10GB to 100GB)_ Lorem ipsum dolor sit amet, consectetur adipiscing elit, " \
                    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, " \
                    "quis nostrud exercitation ."

        temp_info_textblock = TextBlock(temp_info, wrap=True, size=FontSize.SMALL, color=Colors.LIGHT)

        card = AdaptiveCard(
            body=[ColumnSet(columns=[header_column, header_image_column]),
                  FactSet(facts=bot_facts),
                  ColumnSet(columns=[Column(items=[temp_info_textblock, max_tokens_info_textblock], width=2)]),
                  ],
            actions=[OpenUrl(url="https://dashboard.rmi2.managed.netcracker.cloud/", title="Cluster Dashboard")])
        return response_from_adaptive_card(card)


class ClusterInfoCallback(Command):

    def __init__(self):
        super().__init__(
            card_callback_keyword="echo_callback",
            delete_previous_message=True)

    def execute(self, message, attachment_actions, activity):
        return quote_info(attachment_actions.inputs.get("message_typed"))
