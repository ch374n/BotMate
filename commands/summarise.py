from webex_bot.formatting import quote_info, quote_danger
from webex_bot.models.command import Command

from .api import query_summarise
from .utils import get_input_card


def summarise_text(message):
    response = query_summarise(message)
    if 'error' in response or len(response) < 1:
        return quote_danger("could not get the response, please try again.")
    else:
        return quote_info(f"Summary: {response[0]['summary_text']}")


class Summarise(Command):

    def __init__(self):
        super().__init__(
            command_keyword="summarise",
            help_message="Summarise a text",
            chained_commands=[SummariseCallback()])

    def pre_execute(self, message, attachment_actions, activity):
        return quote_info("processing...")

    def execute(self, message, attachment_actions, activity):
        if not message:
            return get_input_card("Summarise a text", "summarise_callback")
        else:
            return summarise_text(message)


class SummariseCallback(Command):

    def __init__(self):
        super().__init__(
            card_callback_keyword="summarise_callback", delete_previous_message=True)

    def execute(self, message, attachment_actions, activity):
        return summarise_text(attachment_actions.inputs.get("text"))
