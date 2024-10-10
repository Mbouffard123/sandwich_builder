# sandwich_class.py
class Sandwich:
    def __init__(self, bread, filling, user_name):
        self.bread = bread
        self.filling = filling
        self.user_name = user_name

    def __str__(self):
        return f"{self.user_name}'s sandwich with {self.filling} on {self.bread} bread."
