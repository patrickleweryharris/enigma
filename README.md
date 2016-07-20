# Enigma
![License](https://img.shields.io/badge/license-MIT-blue.svg) ![python](https://img.shields.io/badge/python-3.5-blue.svg)

The enigma encryption algorithm in python

![Cool Picture](https://raw.githubusercontent.com/patrickleweryharris/enigma/master/img/enigma_machine.jpg)

## Introduction
The enigma machine was one of the most advanced crypto graphical technologies of it's time, possibly the most advanced cryptography humanity has achieved without computers.

Enigma is a type of symmetric encryption. That is, the same key was used to encrypt and decrypt a message. Anyone with this key would be able to encode and decode messages.

This key was constructed by three different parts of the enigma machine.

These are:

  - Rotor settings
  - Ring settings
  - Plug settings

## Enigma Settings

### Rotor Settings

A typical enigma machine had three rotors (which we are simulating here). Rotors could be set up in any starting position, corresponding to a letter in the alphabet.

For example, rotor settings could be `["A", "A", "A"]` or `["B", "Q", "Z"]`

In our simulation here, these will be represented by the ordinal of the these letters (i.e. `["A", "A", "A"]` will be `[65, 65, 65]` and `["B", "Q", "Z"]` will be `[66, 81, 90]`)

### Ring settings

Ring settings alter the configuration of the rotors to ensure that the same letter is not encrypted the same way twice.

Normally, everytime a letter was pressed, the far right rotor (the third) would progress one letter in the alphabet. Once it had gone around a full revolution (through all 26 letters) the middle rotor would then advance one letter in the alphabet.

This process would continue until the middle rotor had gone around a full revolution, which would advance the left hand rotor one position, and so on and so on through the length of the message

The point at which the right rotor made the middle move and the middle made the left move could be changed. These are the ring setting.

A default ring setting on a three rotor enigma machine would be `[26, 26]`

### Plug settings

To add another extra layer of security, every enigma machine was equipped with a plugboard.

This board had ten cables that would switch letter configurations (i.e if "A" was plugged into "B", then typing "A" would use the path normally associated with the letter "B")

An example plug setting could be `[['P','O'], ['M', 'L'], ['I','U'], ['K','J'], ['N','H'], ['Y','T'], ['G','B'], ['V','F'], ['R','E'], ['D','C']]`

Again, for the purposes of this simulation, the ordinals of these letters will be use. So this example ring setting would be
`[[80, 79], [77, 76], [73, 85], [75, 74], [78, 72], [89, 84], [71, 66], [86, 70], [82, 69], [68, 67]]`

## Encrypting and Decrypting

`#TODO`

## Random Stuff

- Messages only accept letters of the alphabet (for now)
