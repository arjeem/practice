import sys

def is_intstring(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def greatestCommonDivisor(a,b):
    if b == 0:
        return a
    else:
        return greatestCommonDivisor(b, a % b)

def leastCommonMultiple(a,b):
    return (a * b) / (greatestCommonDivisor(a,b))

if len(sys.argv) < 3:
    print("Usage: ./LCM.py <int-1> <int-2> (<int-3> ....)")
else:
    if not is_intstring(sys.argv[1]) or int(sys.argv[1]) < 0:
        print("Argument \"{}\" at index {} is not a positive integer.".format(sys.argv[1], 1))
    else:
        lcm = int(sys.argv[1])
        for index in range(2,len(sys.argv)):
            if not is_intstring(sys.argv[index]) or int(sys.argv[index]) < 1:
                print("Argument \"{}\" at index {} is not a positive integer.".format(sys.argv[index], index))
                break
            else:
                lcm = leastCommonMultiple(lcm, int(sys.argv[index]))
        else:
            print("Least common multiple of {} is {}".format(sys.argv[1:len(sys.argv)], lcm))
