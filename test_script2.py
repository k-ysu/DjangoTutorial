class Dog:

    def __init__(self, name, age, furcolor):
        self.name = name
        self.age = age
        self.furcolor=furcolor

    def bark(self , str):
        print("BARK! " + str )

mydog = Dog("John", 20, "Brown")
mydog.bark("Here is Food!")

print(mydog.age)
