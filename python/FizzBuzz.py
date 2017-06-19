import sys

def is_intstring(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if len(sys.argv) != 4:
    print("Usage: ./FizzBuzz.py <fizz-value> <buzz-value> <end-value>")
else:
    for i in range(1,4):
        if not is_intstring(sys.argv[i]) or int(sys.argv[i]) <= 0:
            print ("Argument \"{}\" at position {} is not a postiive integer".format(sys.argv[i], i))
            print ("Please enter positive integers only.")
            break
    fizz = int(sys.argv[1])
    buzz = int(sys.argv[2])

    for i in range(1, int(sys.argv[3])+1):
        if i % fizz == 0:
            if i % buzz == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i % buzz == 0:
            print("Buzz")
        else:
            print(i)
