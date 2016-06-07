class Enigma:
    """
    An enigma machine with rotor, ring and plug settings

    === Attributes ===
    @type rotor_settings: [int]
    @type ring_settings: [int]
    @type plug_settings: [int]
    """

    def __init__(self, rotor_settings, ring_settings, plug_settings):
        """
        Initialize an enigma machine with rotor settings, ring settings
        and plug settings.

        @type self: Enigma
        @type rotor_settings: [int]
        @type ring_settings: [int]
        @type plug_settings: [int]
        @rtype: None
        """
        self.rotor_settings = rotor_settings
        self.ring_settings = ring_settings
        self.plug_settings = plug_settings
