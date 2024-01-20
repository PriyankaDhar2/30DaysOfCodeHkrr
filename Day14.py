class Difference:
    def __init__(self, a):
        self.__elements = a
    def __init__(self, a):
        self.elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        n = len(self.elements)

        max_diff = 0

        for i in range(n):
            for j in range(i + 1, n):
                diff = abs(self.elements[i] - self.elements[j])
                max_diff = max(max_diff, diff)

        self.maximumDifference = max_diff

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)