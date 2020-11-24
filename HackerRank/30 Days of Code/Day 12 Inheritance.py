class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
        self.Person = Person

    def calculate(self):
        avg_grade = sum(scores) / len(scores)
        if avg_grade < 40:
            return "T"
        if avg_grade >= 40 and avg_grade < 55:
            return "D"
        if avg_grade >= 55 and avg_grade < 70:
            return "P"
        if avg_grade >= 70 and avg_grade < 80:
            return "A"
        if avg_grade >= 80 and avg_grade < 90:
            return "E"
        if avg_grade >= 90 and avg_grade <= 100:
            return "O"


firstName = "Heraldo"
lastName = "Memelli"
idNum = 8135627
scores = [100, 80]
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())