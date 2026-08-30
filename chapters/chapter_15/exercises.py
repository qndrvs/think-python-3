## EXERCISES

# 1. Ask a virutal assistant
"""
a. What's the difference between an instance method and a static method?
- Instance method: needs a created object to work. It has access to that object's specific data (its instance variables) and to the context (self). Used when the logic depends on the object's state.
- Static method: belongs to the class itself, not to an individual object. It doesn't have access to any object's data nor to a self context. Used for utilities or logic that doesn't need to know the internal state of any specific instance.

b. Why are static methods called static?
The term "static" (from the Latin staticus, meaning "that which keep its balance") refers to the fact that these methods' behavior is fixe and doesn't change based on an object's state At compile time (or class-loading time), the compiler knows exactl what code to run because it doesn't depend on a specific instanc created at runtime. Unlike instance methods, which are "dynamic" (the can behave differently depending on the data of the object they'r called on), a static method is immutable in its definition an execution: it always does the same thing, no matter how many object exist or what data they hold.

c. Rewrite this function as a method of the Time class
class Time
    def time_to_int(self):
        return self.hour * 3600 + self.minute * 60 + self.second
    def subtract_time(self, other):
        return self.time_to_int() - other.time_to_int()
"""

# 2. Exercise 2
class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year, self.month, self.day = year, month, day
    def __str__(self):
        return f'{self.year:04d}-{self.month:02d}-{self.day:02d}'
    def is_after(self, other) -> bool:
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)
obj1: Date = Date(1933, 6, 22)
obj2: Date = Date(1933, 9, 17)
print(obj1)                    # 1933-06-22
print(obj2.is_after(obj1))     # True