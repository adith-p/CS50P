class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("capacity less than 0")
        self._capacity = capacity

        self.cookie = 0

    def __str__(self):
        return f"{'🍪'*self.cookie}"

    def deposit(self, n):

        if n > self.capacity or self.cookie+n > self.capacity:
            raise ValueError("exceed capacity")

        self.cookie += n

    def withdraw(self, n):
        if n > self.cookie:
            raise ValueError("too many")

        self.cookie -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookie
