"""Python serial number generator."""

class SerialGenerator:
    """Create class to generate serial numbers
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """create new generator"""
        self.start = self.next = start

    def __repr__(self):
        """Use representation built-in"""
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Return next serial number"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset serial numbers"""
        self.next = self.start


