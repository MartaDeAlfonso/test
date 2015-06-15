'''
Cambio
'''


if __name__ == '__main__':

    class Point:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y
        def __str__(self):
            return "x-value " + str(self.x) + " y-value " + str(self.y)
# los guiones bajos son para modificar el operador add de python
#        def __add__(self,other):
        def add(self,other):
            p = Point()
            p.x = self.x+other.x
            p.y = self.y+other.y
            return p
        
p1 = Point(3,4)
p2 = Point(2,3)
print p1
print p1.y

# p1+p2 = p1.add(p2)
#print (p1+p2) 
print p1.add(p2)

