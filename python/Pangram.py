import sys

if len(sys.argv) != 2:
    print("Usage: ./Pangram.py <test-string>")
else:
    testString = sys.argv[1]
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    for c in testString:
        if c in alphabet:
            alphabet.remove(c)
    if not alphabet:
        print("\"{}\" is a pangram.".format(testString))
    else:
        print("\"{}\" is not a pangram.".format(testString))
