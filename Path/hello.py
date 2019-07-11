class test:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.z = self.x + self.y

if __name__ == "__main__":
    a = test(4, 8)
    print(a.x, a.y, a.z)
    a.x = 6
    print(a.z)

