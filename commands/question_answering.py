from webex_bot.formatting import quote_info, quote_danger
from webex_bot.models.command import Command

from .api import query_ask
from .utils import get_input_card, create_payload

table = create_payload()


def ask_question(message):
    payload = {
        "inputs": {
            "query": message,
            "table": table
        }
    }
    response = query_ask(payload)
    if 'error' in response or len(response) < 1:
        return quote_danger("could not get the response, please try again.")
    else:
        return quote_info(f"Answer: {response['answer']}")


class Ask(Command):

    def __init__(self):
        super().__init__(
            command_keyword="ask",
            help_message="Ask a question",
            chained_commands=[AskCallback()])

    def pre_execute(self, message, attachment_actions, activity):
        return quote_info("processing...")

    def execute(self, message, attachment_actions, activity):
        if not message:
            return get_input_card("Ask a question", "ask_callback")
        else:
            return ask_question(message)


class AskCallback(Command):

    def __init__(self):
        super().__init__(
            card_callback_keyword="ask_callback", delete_previous_message=True)

    def execute(self, message, attachment_actions, activity):
        return ask_question(attachment_actions.inputs.get("text"))
