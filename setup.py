from setuptools import setup, find_packages

setup(
    name='BotMate',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'schedule',
        'webex_bot',
        'webexteamssdk',
        'feedparser',
        'requests',
        'urllib3',
        'python-dotenv',
        'sqlalchemy'
    ],
    author='BotMate Team',
    author_email='botmate@netcracker.com',
    description='A Webex based chatbot',
    url='https://git.netcracker.com/sona0421/webex-chatbot',
)
