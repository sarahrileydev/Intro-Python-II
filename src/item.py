class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  def can_eat(self):
    return False

class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories
    def can_eat(self):
        return True