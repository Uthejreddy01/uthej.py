s=input("enter the string")
if s==s[::-1]:
    print("it is palindrome")
else:
    print("not palindrome")
    
    
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test the function
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
