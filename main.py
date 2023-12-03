import os

from dotenv import load_dotenv

load_dotenv()

from commands.cluster_monitoring import ClusterInfo
from commands.more_commands import More
from commands.question_answering import Ask
from commands.summarise import Summarise
from commands.tms_monitoring import TmsMonitoring
from commands.help.translations_help import TranslationHelp
from commands.help.monitoring_help import MonitoringHelp
from webex_bot.webex_bot import WebexBot
from commands.to_english import ToEnglish
from commands.to_russian import ToRussian

from commands.help.custom_help import CustomHelp

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
bot = WebexBot(ACCESS_TOKEN, approved_domains=["netcracker.com"])

if __name__ == "__main__":
    # t1 = threading.Thread(target=run_flask)
    # t1.start()

    bot.commands.remove(bot.help_command)
    bot.commands.add(CustomHelp())
    bot.help_command = CustomHelp
    bot.add_command(Ask())
    bot.add_command(ClusterInfo())
    bot.add_command(TmsMonitoring())
    bot.add_command(Summarise())
    bot.add_command(ToRussian())
    bot.add_command(ToEnglish())
    bot.add_command(More())
    bot.add_command(MonitoringHelp())
    bot.add_command(TranslationHelp())
    bot.run()
