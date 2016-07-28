# Functions for encoding a message with an enigma machine comprised of n rotors

# Could be combined with decode.py using instanced variables
from enigma import Enigma


def _process_messages(msg):
    """
    Sanitize the message to something friendlier to the encryption program

    @type msg: str
    @rtype: None
    """
    cleaned_message = ''
    for char in msg.upper():
        if char.isalpha():
            cleaned_message += char
    return cleaned_message


def _create_ascii_encoding(msg):
    """
    Turn the sanitized message into a version encoded into ordinals.

    @type msg: str
    @rtype: [int]
    """
    returned_list = []
    for char in msg:
        returned_list.append(ord(char) - 65)
    return returned_list


def rotor(machine, message, rotor_num, ring_num):
    """
    Singular function for all rotors of an enigma machine

    @type machine: Enigma
    @type message: [int]
    @type rotor_num: int
    @type ring_num: int
    @rtype: None
    """
    rotor_pos = machine.rotor_settings[rotor_num]
    for char in message:
        char = char + rotor_pos

    # Ring Setting
    machine.rotor_settings[rotor_num] = rotor_pos +\
        _ring(rotor_pos, machine.ring_settings[ring_num])


def _ring(rotor_setting, ring_num):
    """
    Singular function for all rings of an enigma machine

    @type rotor_setting: int
    @type ring_num: int
    @rtype: int
    """
    if ring_num == 0:
        # special condition for first rotor?
        return 0  # Needs to be something different
    if rotor_setting == ring_num:
        return 1

    else:
        return 0


def plugs(machine, message):
    """
    Plug settings of an enigma machine

    Calibrates based on the machine's plug settings

    @type machine: Enigma
    @type message: [int]
    @rtype: None
    """
    for i in range(len(message)):
        for plug in machine.plug_settings:
            if message[i] == plug[0]:
                message[i] = plug[1]


def return_to_string(msg):
    """
    Return a string of the encoded message

    @type msg: [int]
    @rtype: str
    """
    returned_str = ""

    for char in msg:
        returned_str += chr(char + 65)

    return returned_str


# Main encryption function ----------------------------------------------------
def encipher(orig, machine):
    """
    Return an encrypted message

    @type orig: str
    @type machine: Enigma
    @rtype: str
    """
    cleaned_message = _process_messages(orig)
    ascii_message = _create_ascii_encoding(cleaned_message)
    rotor(machine, ascii_message, 0, 0)
    rotor(machine, ascii_message, 1, 1)
    rotor(machine, ascii_message, 2, 2)
    # One of the rotors shouldn't have a ring
    # See special conditions in ring function on line 61
    # Create a special case if the ring number is 0
    plugs(machine, ascii_message)
    end_msg = return_to_string(ascii_message)
    return end_msg
