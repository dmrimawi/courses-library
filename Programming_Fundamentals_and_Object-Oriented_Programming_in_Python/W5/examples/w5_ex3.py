class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking, Art")

class Child(Father, Mother):
    def skills(self):
        print("Child's own skills:")
        super().skills() # This will follow MRO (Method Resolution Order)
        print("Sports")

# Usage
c = Child()
c.skills()
