import sys

if len(sys.argv) == 1:
    print("Usage: ./Isogram.py <string-1> (<string-2> ....)")
else:
    for arg in range(1,len(sys.argv)):
        charList = []
        for c in sys.argv[arg]:
            if c.isalpha():
                if c.lower() in charList:
                    print("\"{}\" is not an isogram.".format(sys.argv[arg]))
                    break
                else:
                    charList.append(c.lower())
        else:
            print("\"{}\" is an isogram.".format(sys.argv[arg]))
