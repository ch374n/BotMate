from webex_bot.formatting import quote_info, quote_danger
from webex_bot.models.command import Command

from .api import query_ru
from .utils import get_input_card


def convert_to_russian(message):
    response = query_ru(message)
    if 'error' in response or len(response) < 1:
        return quote_danger("could not get the response, please try again.")
    else:
        return quote_info(f"**Your input:** {message}\n**Translation:** {response[0]['translation_text']}")


class ToRussian(Command):

    def __init__(self):
        super().__init__(
            command_keyword="ru",
            help_message="Convert text English to Russian",
            chained_commands=[ToRussianCallback()])

    def pre_execute(self, message, attachment_actions, activity):
        return quote_info("processing...")

    def execute(self, message, attachment_actions, activity):
        if not message:
            return get_input_card("Convert text English to Russian", "ru_callback")
        else:
            return convert_to_russian(message)


class ToRussianCallback(Command):

    def __init__(self):
        super().__init__(
            card_callback_keyword="ru_callback", delete_previous_message=True)

    def execute(self, message, attachment_actions, activity):
        return convert_to_russian(attachment_actions.inputs.get("text"))
