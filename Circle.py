class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2
    def perimeter(self):
        return 2 * 3.14 * self.r
def main():
    r = int(input("Enter the radius of the circle: "))
    c = Circle(r)
    print("Area of the circle is: ", c.area())
    print("Perimeter of the circle is: ", c.perimeter())
main()