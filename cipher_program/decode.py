# Functions for decoding a message with a three rotor enigma machine
from enigma import Enigma
from message import Message
import math

DECODE = "d"

def process_messages(msg):
    # TODO sanitize messages


def first_rotor(machine, message):
    """
    The first rotor of an enigma machine

    @type machine: Enigma
    @type message: Message
    @rtype: None
    """
    # TODO first rotor decoding


def second_rotor(machine, message):
    """
    The second rotor of an enigma machine

    @type machine: Enigma
    @type message: Message
    @rtype: None
    """
    # TODO second rotor decoding


def third_rotor(machine, message):
    """
    The third rotor of an enigma machine

    @type macine: Enigma
    @type message: Message
    @rtype: None
    """
    # TODO third rotor decoding


def first_ring(machine, message):
    """
    The first ring of an enigma machine

    Calibrates based on the machine's ring setting

    @type machine: Enigma
    @type message: message
    @rtype: None
    """
    # TODO first ring deconding


def second_ring(machine, message):
    """
    The second ring of an enigma machine

    Calibrates based on the machine's ring setting

    @type machine: Enigma
    @type message: Message
    @rtype: None
    """
    # TODO second ring decoding


def plugs(machine, message):
    """
    Plug settings of an enigma machine

    Calibrates based on the machine's plug settings

    @type machine: Enigma
    @type message: Message
    @rtype: None
    """
    # TODO plug decoding
