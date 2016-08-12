# Functions for decoding a message with a three rotor enigma machine
from enigma import Enigma
import encode  # Decode and encode share some functions


def rotor(machine, message, rotor_num, ring_num):
    """
    Decrypt by rotors

    @type machine: Enigma
    @type message: [int]
    @type rotor_num: int
    @type ring_num: int
    @rtype: None
    """
    rotor_pos = machine.rotor_settings[rotor_num]
    for char in message:
        char = rotor_pos - char  # Should this expression be reversed?

    # Ring Setting
    machine.rotor_settings[rotor_num] = \
        _ring(rotor_pos, machine.ring_settings[ring_num]) - rotor_pos



def _ring(rotor_setting, ring_num):
    """
    Move the rotors if ring setting is reached

    @type rotor_setting: int
    @type ring_num: int
    @rtype: int
    """
    # TODO design ring function for decrypting


def plugs(machine, message):
    """
    Decrypt via the plug settings of an enigma machine

    Calibrates based on the machine's plug settings

    @type machine: Enigma
    @type message: [int]
    @rtype: None
    """
    for i in range(len(message)):
        for plug in machine.plug_settings:
            if message[i] == plug[1]:
                message[i] = plug[0]


# Main decryption function ----------------------------------------------------
def decipher(orig, machine):
    """
    Return a deciphered message

    @type orig: str
    @type machine: Enigma
    @rtype: str
    """
    ascii_message = encode._create_ascii_encoding(orig)
    plugs(machine, ascii_message)
    rotor(machine, ascii_message, 2, 2)
    rotor(machine, ascii_message, 1, 1)
    rotor(machine, ascii_message, 0, 0)
    end_msg = encode.return_to_string(ascii_message)
    return end_msg
