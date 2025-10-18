import math

# Function that reverses a string
def reverse_string(word):
    return ''.join(reversed(word))


# Test. Verification of reverse_string function
def test_reverse_string():
    input_str = "TripleTen"

    # Perform the reverse operation
    reversed_str = reverse_string(input_str)

    # Check if the reversed string matches the expected output
    assert reversed_str == "neTelpirT"

    print("Test Passed! " + input_str + "'s reverse is " + reversed_str)

def is_palindrome(word):
    # Reverse the string using reversed() and join().
     reversed_str = ''.join(reversed(word))
    # Check if the original word is the same as it reversed version.
     return word == reversed_str

def test_is_palindrome():
    input_str = "kayak"
    result = is_palindrome(input_str)
    reversed_str = reverse_string(input_str)
    assert result == True

    print("Test Passed! " + input_str + " is a palindrome.")

def compute_factorial(number):
    # Compute the factorial of "number" using Python's built-in factorial function from the math module.
    return math.factorial(number)

def test_compute_factorial():
    input_number = 5
    result = compute_factorial(input_number)
    assert result == 120
    print("Test Passed! The factorial of " + str(input_number) + " is " + str(result))
