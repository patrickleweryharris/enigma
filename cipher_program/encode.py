# Functions for encoding a message with a three rotor enigma machine
from enigma import Enigma
from message import Message
import math

ENCODE = "e"

def process_messages(msg):
    """
    Sanitize the message to something friendlier to the encryption program

    @type msg: str
    @rtype: None
    """
    cleaned_message = ''
    for char in msg.upper():
        if char.isalpha():  # FIXME Cannot currently handle numbers
            cleaned_message += char
    return cleaned_message


def first_rotor(machine, message):
    """
    The first rotor of an enigma machine

    @type machine: Enigma
    @type message: Message
    @rtype: None
    """
    # TODO first rotor encoding


def second_rotor(machine, message):
    """
    The second rotor of an enigma machine

    @type machine: Enigma
    @type message: Message
    @rtype: None
    """
    # TODO second rotor encoding


def third_rotor(machine, message):
    """
    The third rotor of an enigma machine

    @type macine: Enigma
    @type message: Message
    @rtype: None
    """
    # TODO third rotor encoding


def first_ring(machine, message):
    """
    The first ring of an enigma machine

    Calibrates based on the machine's ring setting

    @type machine: Enigma
    @type message: message
    @rtype: None
    """
    # TODO first ring encoding


def second_ring(machine, message):
    """
    The second ring of an enigma machine

    Calibrates based on the machine's ring setting

    @type machine: Enigma
    @type message: Message
    @rtype: None
    """
    # TODO second ring encoding


def plugs(machine, message):
    """
    Plug settings of an enigma machine

    Calibrates based on the machine's plug settings

    @type machine: Enigma
    @type message: Message
    @rtype: None
    """
    # TODO plug encoding
