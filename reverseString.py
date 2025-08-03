# Ashlyn Croft
# 3rd aug 25
# Lab 11
# Reverse a string using both iterative & recursive approaches





def reverseIterative(inputString):
    """
    Reverse a string using a for loop without range() function (iterative approach).
    Based on my previous reverseString function.
    
    inputString - the string to reverse (string)
    
    Returns the reversed string (string)
    """
    reversedString = ""



    for char in inputString:
        reversedString = char + reversedString
    return reversedString




def reverseRecursive(inputString):
    """
    Reverse a string using recursion (no loops).
    Base case: empty string returns empty string
    Recursive case: reverse the rest + first character
    
    inputString - the string to reverse (string)
    
    Returns the reversed string (string)
    """


    if len(inputString) <= 1:
        return inputString
    



    return reverseRecursive(inputString[1:]) + inputString[0]






def main():
    """
    Main function that gets user input and demonstrates both string reversal methods.
    """
    print("String Reversal Demonstration")
    print("=" * 40)
    print("This program shows 2 different ways to reverse a string.")
    print("Example: 'APPLE CAT!' becomes '!TAC ELPPA'")
    print()
    

    userString = input("Enter a string to reverse: ")
    print()
    print("Original string:", userString)
    print("-" * 40)
    

    result1 = reverseIterative(userString)
    print(f"Iterative method: {result1}")
    


    result2 = reverseRecursive(userString)
    print(f"Recursive method: {result2}")
    
    print("-" * 40)
    



    if result1 == result2:
        print("✓ Success! Both reversal methods work correctly.")
    else:
        print("⚠ Warning: Methods produced different results!")
    




    print(f"\nDebug info:")
    print(f"Original length: {len(userString)}")
    print(f"Reversed length: {len(result1)}")
    print(f"First char becomes: '{userString[0] if userString else 'N/A'}' → '{result1[-1] if result1 else 'N/A'}'")





if __name__ == "__main__":
    main()