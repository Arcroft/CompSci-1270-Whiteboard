# Ashlyn Croft
# 3rd Aug
# Lab 11
# Palindrome check
# Adding recursive method

def isPalindromeIterative(inputString):
    """
    Check if a string is a palindrome by comparing characters iteratively.
    Based on my previous palindromeCheck function.
    """

    stringLength = len(inputString)
    

    for i in range(stringLength // 2):


        if inputString[i] != inputString[stringLength - 1 - i]:
            return False
    

    return True





def isPalindromeRecursive(inputString):
    """
    Check if a string is a palindrome using recursion.
    Base case: strings of length 0 or 1 are palindromes
    Recursive case: first and last chars must match, and middle must be palindrome
    """



    if len(inputString) <= 1:
        return True
    


    if inputString[0] != inputString[-1]:
        return False
    


    return isPalindromeRecursive(inputString[1:-1])






def main():
    """
    Main function that gets user input and demonstrates both palindrome checking methods.
    """
    print("Palindrome Checker")
    print("=" * 40)
    print("This program checks if a string reads the same forwards and backwards.")
    print("Example: 'mom' is a palindrome, 'hello' is not")
    

    userString = input("Enter a string to check: ")
    print()
    print("Original string:", userString)
    print("-" * 40)



    result1 = isPalindromeIterative(userString)
    if result1:
        print("Iterative method: ✓ PALINDROME")
    else:
        print("Iterative method: ✗ NOT a palindrome")
    



    result2 = isPalindromeRecursive(userString)
    if result2:
        print("Recursive method: ✓ PALINDROME")
    else:
        print("Recursive method: ✗ NOT a palindrome")
    
    print("-" * 40)
    


    if result1 == result2:
        print("✓ Both methods agree on the result!")
    else:
        print("⚠ Warning: Methods produced different results!")
    



    print(f"\nDebug info:")
    print(f"String length: {len(userString)}")
    print(f"First character: '{userString[0] if userString else 'N/A'}'")
    print(f"Last character: '{userString[-1] if userString else 'N/A'}'")

if __name__ == "__main__":
    main()