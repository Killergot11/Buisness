#def functions
def areaOfSquare(param):
    return("Area of square is: " + str(int(param['side'])**2))

def perimeterOfSquare(param):
    return("Perimeter of square is: " + str(int(param['side'])*4))

def areaOfRectangle(param):
    return("Area of rectangle is: " + str(int(param['length'])*int(param['breadth'])))

def perimeterOfRectangle(param):
    return("Area of rectangle is: " + str(2*(int(param['length'])+int(param['breadth']))))

def areaOfCircle(param):
    return("Area of circle is: " + str(3.14*(int(param['radius'])**2)))

def perimeterOfCircle(param):
    return("Area of circle is: " + str(2*3.14*int(param['radius'])))

def areaOfTriangle(param):
    return("Area of triangle is: " + str(0.5*(int(param['breadth'])*int(param['height']))))
    
# def perimeterOfTriangle(param):
    # return("Area of square is: " + str(s1+s2+s3))