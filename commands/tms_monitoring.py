import logging

from webex_bot.formatting import quote_info, quote_warning
from webex_bot.models.command import Command

from database import is_monitoring_enabled
from .utils import is_part_of_group, get_tms_input_card

log = logging.getLogger(__name__)


class TmsMonitoring(Command):

    def __init__(self):
        super().__init__(
            command_keyword="tms_monitoring",
            help_message="Enable/Disable TMS monitoring",
            chained_commands=[TmsMonitoringCallback()])
        self.monitoring_name = 'tms_monitoring'

    def pre_execute(self, message, attachment_actions, activity):
        return quote_info("processing...")

    def execute(self, message, attachment_actions, activity):
        # get the room id
        # check if monitoring is enabled for roomid
        # if yes show message
        # if not then check if user is part of group
        # if yes then
        # ask for project-id/userid
        # if no then show unauthorized
        room_id = attachment_actions.roomId
        if is_monitoring_enabled(self.monitoring_name, room_id):
            return quote_info("monitoring is already enabled")
        elif is_part_of_group(attachment_actions.personId):
            return get_tms_input_card()
        else:
            return quote_warning("you are not authorized to perform this action")


class TmsMonitoringCallback(Command):

    def __init__(self):
        super().__init__(
            card_callback_keyword="tms_monitoring_callback",
            delete_previous_message=True)

    def execute(self, message, attachment_actions, activity):
        return quote_info("cool, tms monitoring is now enabled")
