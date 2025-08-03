#Ashlyn Croft
# Aug3 2025
# LAb 11
# White board tasks
# Examining ways to do code sum solutions.
# Tutorial on https://interviewing.io/questions/two-sum





def twoSumLoops(nums, target):
    """
    Naive approach: Check every pair of numbers using nested loops
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]  
    return None 





def twoSumDict(nums, target):
    """
    Efficient approach: Use a dictionary to store numbers we've seen
    """
    seen = {}  
    
    for i, num in enumerate(nums):
        complement = target - num  
        
        if complement in seen:
            return [seen[complement], i]  
        
        seen[num] = i  
    
    return None  





def twoSumLoopsAll(nums, target):
    """
    Find ALL possible pairs using nested loops
    Returns list of [index1, index2] pairs
    """
    all_pairs = []
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                all_pairs.append([i, j])
    
    return all_pairs





def twoSumDictAll(nums, target):
    """
    Find ALL possible pairs using dictionary approach
    Returns list of [index1, index2] pairs
    """
    all_pairs = []
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            for prev_index in seen[complement]:
                all_pairs.append([prev_index, i])
        

        if num not in seen:
            seen[num] = []
        seen[num].append(i)
    
    return all_pairs

def main():
    nums = [2, 7, 11, 15, 3, 6]
    target = 9
    
    print(f"Numbers: {nums}")
    print(f"Target: {target}")
    print()
    


    result1 = twoSumLoops(nums, target)
    print(f"twoSumLoops result: {result1}")
    
    result2 = twoSumDict(nums, target)
    print(f"twoSumDict result: {result2}")
    print()
    


    result3 = twoSumLoopsAll(nums, target)
    print(f"twoSumLoopsAll result: {result3}")
    
    result4 = twoSumDictAll(nums, target)
    print(f"twoSumDictAll result: {result4}")

if __name__ == "__main__":
    main()