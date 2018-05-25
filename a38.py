#find the area and perimeter of a circle

class Circle:
  def area(self):
    return 3.14 * self.radius **2
  def perimeter(self):
    return 3 **2 * self.radius
  def __init__ (self, radius):
    self.radius = radius
    
x = Circle(5)

print(x.area())
print(x.perimeter())
