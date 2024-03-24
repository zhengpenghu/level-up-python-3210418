
def is_palindrome(input):
    forward = [c.lower() for c in input if c.isalnum()]
    backward = forward[::-1]
    return forward == backward


# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
