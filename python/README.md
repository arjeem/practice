# Problems

## FizzBuzz
``` Usage (Command Line): ./Fizzbuzz.py <Fizz> <Buzz> <Range> ```

Given 3 positive integers:
  * `Fizz`
  * `Buzz`
  * `Range`
For all numbers `n` in `[1,Range]`:
1. If `n` is divisible by `Fizz`, print "Fizz"
2. If `n` is divisible by `Buzz`, print "Buzz"
3. If `n` is divisible by both, print "FizzBuzz"
4. Else, print `n`

## Isogram
``` Usage (Command Line): ./Isogram.py <String-1> (<String-2> ...) ```
#### Definition: An isogram is a string in which no letters appear more than once
For each `<String-n>` passed to the program:
 * Print `<String-n>` and whether or not it is an isogram
 
Considerations:
  * Non-alphabetic characters do not matter in determining an isogram. Ex: *I--2--2-n* is an isogram
