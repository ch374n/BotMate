import csv
import os

from webex_bot.models.response import response_from_adaptive_card
from webexteamssdk import WebexTeamsAPI
from webexteamssdk.models.cards import Text, FontWeight, TextBlock, Column, AdaptiveCard, ColumnSet, FontSize, Choices, \
    Choice, Toggle, FactSet, Fact, Image, ImageSize, ImageStyle
from webexteamssdk.models.cards.actions import Submit

csv_file_path = 'resources/data.csv'

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
WEBEX_SPACE_ID = os.getenv('WEBEX_SPACE_ID')

webex_api = WebexTeamsAPI(access_token=ACCESS_TOKEN)


def get_input_card(heading, callback_keyword):
    input_field = Text(id="text", isMultiline=True, placeholder="please enter text")
    submit = Submit(title="Submit",
                    data={
                        "callback_keyword": callback_keyword})
    heading = TextBlock(heading, weight=FontWeight.BOLDER, wrap=True, size=FontSize.SMALL)
    header_column = Column(items=[heading, input_field], width=2)
    card = AdaptiveCard(
        body=[ColumnSet(columns=[header_column])
              ],
        actions=[submit])
    return response_from_adaptive_card(card)


def get_tms_input_card():
    input_field = Text(id="text", placeholder="Enter TMS id e.g CMDEV")
    submit = Submit(title="Submit",
                    data={
                        "callback_keyword": "tms_monitoring_callback"})
    heading = TextBlock("Enable TMS monitoring", weight=FontWeight.BOLDER, size=FontSize.MEDIUM)

    image = Image(
        url="https://i.imgur.com/ycIQYjY.png",
        style=ImageStyle.PERSON,
        size=ImageSize.AUTO)

    header_image_column = Column(
        items=[image],
        width=1,
    )

    header_column = Column(items=[heading], width=2)

    headers = ColumnSet(columns=[header_column, header_image_column])
    choices = Choices(
        id="Type",
        value="PERSONAL",
        choices=[Choice(title="PERSONAL TMS", value="PERSONAL"), Choice(title="PROJECT TMS", value="PROJECT")],
    )

    params = [Fact(title="TMS ID", value="User id or project id"),
              Fact(title="Type", value="Whether to enable for personal or project"),
              Fact(title="Critical/Blocker", value="What priority tickets to enable")]

    card = AdaptiveCard(
        body=[
            headers,
            FactSet(facts=params),
            input_field,
            choices,
            Toggle(id="blocker", title="Blocker"),
            Toggle(id="critical", title="Critical")
        ],
        actions=[submit])
    return response_from_adaptive_card(card)


def create_payload():
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

        # Get the header row
        header = rows[0]

        # Initialize the result structure
        result = {}

        # Iterate through each header column
        for column_index, column_name in enumerate(header):
            result[column_name] = []

            # Iterate through each row and append the value to the corresponding column
            for row in rows[1:]:
                result[column_name].append(row[column_index])

        # Print the result

        table = {}
        for column_name, values in result.items():
            table[column_name] = values
    return table


def is_part_of_group(person_id):
    return any(member.personId == person_id for member in webex_api.memberships.list(roomId=WEBEX_SPACE_ID))
