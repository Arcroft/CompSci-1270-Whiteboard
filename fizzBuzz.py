# Ashlyn Croft
# 3rd Aug. Idk. Suppose I passed midnight.
# Lab 11
# fizzBuzz 'game'
# Different ways to react to numbers in cycle

# I think I might have really had fun with this lab if it was a 15 week course. This seem like great ways to really explore, and right now all I care about is getting this done so I can sleep.





def fizzBuzzModulus(n):
    """
    Solves FizzBuzz using modulus operator approach
    Based on: https://www.enjoyalgorithms.com/blog/fizz-buzz-problem
    Accessed: 2AUG25
    
    Rules:
    - Fizz for multiples of 3
    - Buzz for multiples of 5  
    - Bazz for multiples of 7
    - Combinations for multiple conditions (e.g., FizzBuzz for 15)
    """
    output = []
    
    for i in range(1, n + 1):
        result = ""
        

        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if i % 7 == 0:
            result += "Bazz"
            

        if result == "":
            result = str(i)
            
        output.append(result)
    
    return output






def fizzBuzzDict(n):
    """
    Solves FizzBuzz using dictionary/hash table approach
    Based on: https://www.enjoyalgorithms.com/blog/fizz-buzz-problem
    Accessed: 2AUG25

    """
    output = []
    

    fizz_buzz_mapping = {
        3: "Fizz",
        5: "Buzz", 
        7: "Bazz"
    }
    
    for i in range(1, n + 1):
        result = ""
        

        for divisor, word in fizz_buzz_mapping.items():
            if i % divisor == 0:
                result += word
        



        if result == "":
            result = str(i)
            

        output.append(result)
    


    return output








def main():
    """
    Main function to get user input and test both approaches
    """
    try:
        n = int(input("Enter a positive integer: "))
        
        if n <= 0:
            print("Please enter a positive integer.")
            return
            


    except ValueError:
        print("Please enter a valid integer.")
        return
    
    print(f"\nFizzBuzz for numbers 1 to {n}:")
    print("=" * 40)
    


    # modulus approach
    print("Modulus Approach Results:")
    result1 = fizzBuzzModulus(n)
    print(result1)
    
    # dict approach
    print("\nDictionary Approach Results:")
    result2 = fizzBuzzDict(n)
    print(result2)
    

    # Verify both approaches
    if result1 == result2:
        print("\n✓ Both approaches produce identical results!")
    else:
        print("\n⚠ Warning: Results differ between approaches!")



if __name__ == "__main__":
    main()



# I forgot one was Bazz, not Buzz, and got pissed off it was seemingly randomly changing spelling.
# So, Probably need sleep.