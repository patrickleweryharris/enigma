# Enigma
![License](https://img.shields.io/badge/license-MIT-blue.svg) ![python](https://img.shields.io/badge/python-3.5-blue.svg)

The enigma encryption algorithm in python

##### Table of Contents

[Introduction](https://github.com/patrickleweryharris/enigma#introduction)  
[Enigma Settings](https://github.com/patrickleweryharris/enigma#enigma-settings)  
[Encrypting and Decrypting](https://github.com/patrickleweryharris/enigma#encrypting-and-decrypting)  
[Random Stuff](https://github.com/patrickleweryharris/enigma#random-stuff)  

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

In our simulation here, these will be represented by the ordinal of the these letters (i.e. `["A", "A", "A"]` will be `[0, 0, 0]` and `["B", "Q", "Z"]` will be `[1, 16, 26]`)

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
`[[15, 14], [12, 11], [8, 20], [10, 9], [13, 7], [24, 19], [6, 1], [21, 5], [17, 4], [3, 2]]`

By convention, no letter is mentioned more than once in plug settings, i.e. `[['A', 'E'], ['E', 'A']]` is not  a valid plug setting

## Encrypting and Decrypting

### Encrypting a file

#### Message file

The message file can be any text file. Non alphabetic characters and spaces will be stripped by the encryption process.

Messages should be constructed like old style telegraphs:

`THIS IS MY MESSAGE STOP ARRIVE BY FOUR FORTY FIVE STOP`


#### Enigma machine file
The enigma machine file should only have three lines. The first line is the rotor settings, the second the ring settings and the third is the plug settings.

An example of an enigma file:

```python
[0, 0, 0]
[26, 26]
[[15, 14], [12, 11], [8, 20], [10, 9], [13, 7], [24, 19], [6, 1], [21, 5], [17, 4], [3, 2]]
```

## Random Stuff

- Messages only accept letters of the alphabet (for now)
