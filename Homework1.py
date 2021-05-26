import math

def pyramid(s):
        """
        Prints a “message pyramid” for the input message string starting from the first character in the string.
        """
        pyramid = ''
        for letter in s:
                pyramid += letter
                print(pyramid)

def findSquares(s:int = 0, e:int = 0):
        """          
        Print numbers which are exact squares of an integer within range of two integers.
        Return list of numbers that perfect squares.
        """
        # check to see if either input is negative and return error message
        if s < 0 or  e < 0:
                return "Invalid Input. Unable to take square root of negative number."
        squares = []
        if s > e:
                for num in range(e,s+1):
                        square_root = str(math.sqrt(num)).split('.')
                        if square_root[1] == '0':
                                squares.append(num)
        elif s < e:
                for num in range(s,e+1):
                        square_root = str(math.sqrt(num)).split('.')
                        if square_root[1] == '0':
                                squares.append(num)
        else:
                        square_root = str(math.sqrt(s)).split('.')
                        if square_root[1] == '0':
                                squares.append(s)
        print(squares)
        return squares

def calSalary(h:float,r:float = 20):
        """
        Return the salary in float. h is number of hours and r is the hourly rate.
        If the rate is not specified use the default rate to be $20 / hour.
        If the hours are less than zero print("Not valid Hours") and return -1.
        """
        if h < 0:
                print("Not valid Hours")
                return -1
        elif h >= 0 and h <= 40:
                salary = h*r
                return salary
        else:
                salary = 40*r + (h-40)*(r*1.2)
                return salary

def calLetterGrade(points,gradescale):
        """

        """