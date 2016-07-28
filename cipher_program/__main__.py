"""
Encrypt or decrypt the contents of a message file using an enigma machine.
"""
import encode
import decode
from enigma import Enigma
import os.path

ENCODE = "e"
DECODE = "d"

# FIXME still using some old file names


def get_valid_filename(msg):
    """
    Prompt the user, using msg, to type the name of a file. This file should
    exist in the same directory as the starter code. If the file does not
    exist, keep re-prompting until they give a valid filename.
    Return the name of that file.

    @type msg: str
    @rtype: str
    """
    filename = input(msg)
    while not os.path.exists(filename):
        print("That file does not exist.")
        filename = input(msg)
    return filename


def get_encryption_mode():
    """
    Prompt the user to enter the encryption mode. If the user enters an invalid
    mode, keep re-prompting until they give a valid mode.

    @type (): user input
    @rtype: str
    """
    msg = 'Do you want to encrypt ({0}) or decrypt ({1})? '.format(
        encode.ENCODE, decode.DECODE)
    mode = input(msg)
    while not (mode == encode.ENCRYPT or
               mode == decode.DECRYPT):
                print('Invalid mode.')
                mode = input(msg)
    return mode


def is_valid_machine(machine):
    """
    Return true iff an enigma file has valid plug, ring and rotor settings

    @type machine: Enigma
    @rtype: bool
    """
    # General checks

    if type(machine) != Enigma:  # FIXME Will this work??
        return False

    # Plug checks:

    # TODO need to add checks for valid plug setting
    # see 'by convention' blurb in README.md
    if len(machine.plug_settings != 10):
        return False

    for plug in machine.plug_settings:
        if len(plug) != 2 or type(plug[0]) != int or type(plug[1]) != int:
            return False

    # Rotor Checks

    if len(machine.rotor_settings) != 3 or\
        type(machine.rotor_settings[0]) != int or\
        type(machine.rotor_settings[1]) != int or\
            type(machine.rotor_settings[2]) != int:
        return False

    for rotor in machine.rotor_settings:
        if rotor not in range(0, 27):
            return False

    # Ring Checks
    if len(machine.ring_settings) != 2 or\
        type(machine.ring_settings[0]) != int or\
            type(machine.ring_settings[1]) != int:
        return False

    for ring in machine.ring_settings:
        if ring not in range(0, 27):
            return False

    return True


def main():
    """
    Perform the encryption using the machine from file named MACHINE_FILENAME
    and the message from file named MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    prompt = 'Enter the name of the file that contains the enigma machine: '
    enigma_file = open(get_valid_filename(prompt), 'r')
    enigma_machine = something  # TODO Create an engima machine from the file
    enigma_file.close()
    if not (is_valid_machine(enigma_machine)):
        print('The supplied file is not a valid enigma machine.')
        print('Encryption process stopping.')
        return

    prompt = 'Enter the name of the file that contains the message: '
    msg_file = open(get_valid_filename(prompt), 'r')
    messages = something  # TODO need to redo this entire function
    msg_file.close()

    mode = get_encryption_mode()
    if mode == DECODE:  # FIXME update these calls to the new functions
        for msg in decode.process_messages(enigma_machine, messages, mode):
            print(msg)

    if mode == ENCODE:
        print(encode.encipher(messages, enigma_machine))

if __name__ == "__main__":
    main()
