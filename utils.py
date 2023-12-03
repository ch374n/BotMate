import re

pattern = r'(?<=/)([A-Z]+-\d+)'


def get_priority_emoji(priority):
    if priority == "Normal":
        return "⬇️"
    elif priority == "Low":
        return "🔽"
    elif priority == "Major":
        return "🔸"
    elif priority == "Critical":
        return "❗"
    else:
        return "🚫"


def get_type_emoji(type):
    if type == "Task":
        return "☑️"
    elif type == "Defect":
        return "🔴"
    elif type == "Dev Task":
        return "⚙️"
    elif type == "Epic":
        return "⚛️"
    elif type == "Action Item":
        return "❇️"
    else:
        return "📌"


def get_type(id):
    if id == '1':
        return 'Defect'
    elif id == '9':
        return 'Dev Task'
    elif id == '15':
        return 'Task'
    elif id == '16':
        return 'Epic'
    elif id == '17':
        return 'Story'
    else:
        return 'Action Item'


def get_priority(id):
    if id == '1':
        return 'Blocker'
    elif id == '2':
        return 'Critical'
    elif id == '3':
        return 'Major'
    elif id == '4':
        return 'Normal'
    else:
        return 'Low'


def get_key(link):
    match = re.search(pattern, link)
    if match:
        ticket_number = match.group(1)
        return ticket_number
    raise ValueError('Invalid link')
