
class SerialGenerator:

    def __init__(self,start =0)
        """Making a new generator, starting at start."""
        self.start = self.next = start
    def __repr__(self):
        return f"<Serial Generator start ={self.start} next={self.next}>"
    def generate(self):
        self.next += 1
        return self.next -1
    def reset(self):
        self.next = self.start