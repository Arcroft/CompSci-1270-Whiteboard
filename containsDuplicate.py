#Ashlyn Croft
# 2Aug25
# Checks for duplicates

# If you "borrow" any of the code found in the readings above to complete the tasks below, or if
# you take code from any source that is not original to you, you must provide proper citation/ attribution.
# This includes the author's name, the date the article was written (if available), when you accessed the
# article, and the URL where the article can be found. Place this citation in comments for the function that
# the code appears in

# I don't understand this at all. 
# Like, if I read shakespeare and quote shakespeare, yes, I have to cite.
# But if I use the word verily I don't.
# So if I copy and paste code: cite. But, If I follow a tutorial and use common commands?
# If I watch a video titled: "How to write the sentence: "Where has my cat gone"?"
# And I write the sentence, "Where has my cat gone", I don't need to cite?

# Idk.
# Used NEET tutorial 2ndaug

class Solution:
    # Solution approach learned from NeetCode video tutorial
    # "Contains Duplicate" - accessed 2nd aug
    # https://neetcode.io/
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
