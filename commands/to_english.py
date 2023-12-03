from webex_bot.formatting import quote_info, quote_danger
from webex_bot.models.command import Command

from .api import query_en
from .utils import get_input_card


def convert_to_english(message):
    response = query_en(message)
    if 'error' in response or len(response) < 1:
        return quote_danger("не удалось получить ответ, попробуйте еще раз.")
    else:
        return quote_info(f"Translation: {response[0]['translation_text']}")


class ToEnglish(Command):

    def __init__(self):
        super().__init__(
            command_keyword="en",
            help_message="Convert Russian text to English",
            chained_commands=[ToEnglishCallback()])

    def pre_execute(self, message, attachment_actions, activity):
        return quote_info("processing...")

    def execute(self, message, attachment_actions, activity):
        if not message:
            return get_input_card("Convert Russian text to English", "en_callback")
        else:
            return convert_to_english(message)


class ToEnglishCallback(Command):

    def __init__(self):
        super().__init__(
            card_callback_keyword="en_callback", delete_previous_message=True)

    def execute(self, message, attachment_actions, activity):
        return convert_to_english(attachment_actions.inputs.get("text"))
