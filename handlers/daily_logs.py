import discord
import log
import os
from datetime import datetime

_CURRENT_DIR = os.path.dirname(os.path.dirname(__file__))
_LOG_DIR = os.path.join(_CURRENT_DIR, "res", "textfiles", "logs")
_FILE_PATH = None


def _init_logs():
    global _FILE_PATH
    now = datetime.utcnow()  # current date and time
    current_time = now.strftime("%m-%d-%Y:%Hhr.%Mm.%Ss")
    _FILE_PATH = os.path.join(_LOG_DIR, f"{current_time}.txt")


_init_logs()


def getRoles(member: discord.Member):
    return [str(role.name) for role in member.roles]


def analytics(message: discord.Message):
    user_message = message.content
    if len(user_message) > 0 and user_message[0] in ("/", '!', '?') and not message.author.bot:
        now = datetime.utcnow()  # current date and time
        current_time = now.strftime("%m-%d-%Y:%Hhr.%Mm.%Ss")

        log.debug(
            f"""[LOG] LOGGING MESSAGE SENT BY {message.author} ON {current_time} """)

        log_file = open(_FILE_PATH, 'a+')

        role_list = getRoles(message.author)

        log_data = {
            'date': current_time,
            'command': user_message,
            'roles': role_list,
            'author': str(message.author)
        }

        log_file.write(f'{str(log_data)}\n')
        # log_file.write(
        #     f"""[{dt.now()}] MESSAGE: {message.content}, TYPE: command, AUTHOR: {message.author}, ROLES: {", ".join(roles)} \n""")

        log_file.close()
