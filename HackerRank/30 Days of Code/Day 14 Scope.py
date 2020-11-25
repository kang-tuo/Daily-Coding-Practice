class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        max_diff = 0
        for element1 in self.__elements:
            for element2 in self.__elements:
                diff = abs(element1 - element2)
                self.maximumDifference = max(max_diff, diff)
                max_diff = self.maximumDifference


# End of Difference class


a = [1, 2, 5]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)