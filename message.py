class Message:
    """
    A message to be encrypted or decrypted
    """

    def __init__(self, message, ring_setting, start_position, plug_setting):
        """
        Initate a message and key settings

        @param self: Message
        @param message: str
        @param ring_setting: str
        @param start_position: str
        @param plug_setting: list
        @rtype: None

        >>> m1 = Message('Hello World',
        'AAA', 'AAA',
        ['PO', 'ML', 'IU', 'KJ', 'NH', 'YT', 'GB', 'VF', 'RE', 'DC'])
        >>> m1.message
        'Hello World'
        >>> m1.keysetting
        {'Ring Setting': 'AAA',
        'Start Position': 'AAA',
        'Plug Setting': ['PO', 'ML', 'IU', 'KJ', 'NH', 'YT', 'GB', 'VF', 'RE', 'DC']}
        """
        self.message = message
        self.keysetting = {'Ring Setting': ring_setting,
                           'Start Position': start_position,
                           'Plug Setting': plug_setting}

    def __str__(self):
        """
        Return a string representation of a message and keysetting

        @param self: Message
        @rtype: str

        >>> m1 = Message('Hello World', 'AAA', 'AAA', ['PO', 'ML', 'IU', 'KJ', 'NH', 'YT', 'GB', 'VF', 'RE', 'DC'])
        >>> print(m1)
        --- Begin Message ---
        Hello World
        <BLANKLINE>
        --- Begin Keysetting ---
        Ring Setting: AAA
        Start Position: AAA
        Plug Setting: PO ML IU KJ NH YT GB VF RE DC
        """
        plugs = ''
        for setting in self.keysetting['Plug Setting']:
            plugs = plugs + ' ' + setting

        returned_str = '--- Begin Message ---\n{0}\n\n--- Begin Keysetting ---\nRing Setting: {1}\nStart Positon: {2}\nPlug Setting:{3}'.format(
            self.message,
            self.keysetting['Ring Setting'],
            self.keysetting['Start Position'],
            plugs)
        return returned_str


if __name__ == '__main__':
    import doctest
    doctest.testmod()
