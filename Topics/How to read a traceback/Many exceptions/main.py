import math

def find_sqrt(number):
    try:
        try:
            print(math.sqrt(number))
        except TypeError:        
            print(math.sqrt(int(number)))
    except ValueError:
        print('Please pass a number like "5" or 5')
    
