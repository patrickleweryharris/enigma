# Functions for decoding a message with a three rotor enigma machine
from enigma import Enigma
import encode  # Decode and encode share some functions


# Main decryption function ----------------------------------------------------
def decipher(orig, machine):
    """
    Return a deciphered message

    @type orig: str
    @type machine: Enigma
    @rtype: str
    """
    # TODO encode.create_ascii_encoding etc...
