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


def rotor(machine, message, rotor_num, ring_num):  # FIXME Rename to reflect that this method is now ring and rotor
    """
    Singular function for all rotors of an enigma machine

    @type machine: Enigma
    @type message: [int]
    @type rotor_num: int
    @type ring_num: int
    @rtype: None
    """
    rotor_pos = machine.rotor_settings[rotor_num]
    starting_pos = rotor_pos
    for char in message:
        char = char + rotor_pos
        rotor_pos += 1
        if rotor_pos - 26 == starting_pos:  # Hardcoded ring setting
            rotor_pos = starting_pos  # Makes the rotors circular
            next_rotor = _get_next_rotor(rotor_num)
            if next_rotor == 1 or next_rotor == 2:
                machine.rotor_settings[rotor_num + 1] += 1


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
    # FIXME Ring function is no longer needed. Has been hardcode in line 49


def _get_next_rotor(rotor_num):
    """
    Get the next rotor to move

    @type rotor_num: int
    @rtype: int
    """
    if rotor_num == 0:
        return 1
    elif rotor_num == 1:
        return 2
    else:
        return 0


def plugs(machine, message):
    """
    Encrypt via the plug settings of an enigma machine

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

    # This program is currently hardcoded to a three rotor enigma variant,
    # though it is compleatly extensible
