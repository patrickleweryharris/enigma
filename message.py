class Message:
    """
    A message to be encrypted or decrypted

    === Attributes ===
    @type content: str
    """

    def __init__(self, content):
        """
        Initialize a message

        @type self: Message
        @type content: str
        @rtype: None
        """
        self.content = content

    def __str__(self):
        """
        Return a string representation

        @type self: Message
        @rtype: str
        """
        return self.content
