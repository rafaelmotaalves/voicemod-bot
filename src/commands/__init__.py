from telegram.ext import CommandHandler, Dispatcher

from commands.get_mod import GetModCommand
from commands.set_mod import SetModCommand
from commands.list_mods import ListModsCommand

COMMANDS = [
    CommandHandler(SetModCommand.command, SetModCommand().callback),
    CommandHandler(GetModCommand.command, GetModCommand().callback),
    CommandHandler(ListModsCommand.command, ListModsCommand().callback)
]

def register_commands(dispatcher: Dispatcher):
    for command in COMMANDS:
        dispatcher.add_handler(command)