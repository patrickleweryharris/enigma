"""
Encrypt or decrypt the contents of a message file using an enigma machine.
"""
import encode
import decode
import os.path

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

def main():
    """
    Perform the encryption using the deck from file named DECK_FILENAME and
    the message from file named MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """

    prompt = 'Enter the name of the file that contains the enigma machine: '
    enigma_file = open(get_valid_filename(prompt), 'r')
    enigma_machine =  # TODO
    enigma_file.close()
    if not (cipher_functions.is_valid_deck(deck)):
        print('The supplied file is not a valid enigma machine.')
        print('Encryption process stopping.')
        return

    prompt = 'Enter the name of the file that contains the message: '
    msg_file = open(get_valid_filename(prompt), 'r')
    messages =  # TODO
    msg_file.close()

    mode = get_encryption_mode()
    if mode == DECRYPT:
        for msg in decode.process_messages(enigma_machine, messages, mode):
            print(msg)

    if mode == ENCRYPT:
        for msg in enocode.process_messages(enigma_machine, messages, mode):
            print(msg)

if __name__ == "__main__":
    main()
