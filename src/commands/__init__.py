from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler

from commands.get_mod import GetModCommand
from commands.set_mod import SetModCommand
from commands.list_mods import ListModsCommand
from commands.modify_audio import ModifyAudioHandler
from dal.audio_repository import TelegramAudioRepository

COMMANDS = [
    CommandHandler(SetModCommand.command, SetModCommand().callback),
    CommandHandler(GetModCommand.command, GetModCommand().callback),
    CommandHandler(ListModsCommand.command, ListModsCommand().callback),
    MessageHandler(Filters.voice, ModifyAudioHandler(TelegramAudioRepository()).callback),
]

def register_commands(dispatcher: Dispatcher):
    for command in COMMANDS:
        dispatcher.add_handler(command)