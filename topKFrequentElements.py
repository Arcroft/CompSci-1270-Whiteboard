#Ashlyn Croft
# Idk. August. 2nd.
# Frequency checls
#neet tutorial 2nd aug



# I do 20 credits in a regular semester and am bored. 
# I'm in a stats book club
# I'm in several phil/stat pursuits outside requirements
# Pro bono stats work
# Side stylometry writing analysis project to get better at stylometry and python - then throw it up open source
# I like education -alot-.
# 9 credits of stem in 8 week summer? I honestly want to drop out of school.
# Seriously this is such a miserable experience it's making me hate python, ISU, and academia. It's been 8 weeks of a project due every single day. M, T, W, Th, F, Sa, Su. For 8 weeks.
# My dog has been in the animal hospital. I was sitting in the lobby at 3am thinking "well, at least by not sleeping tonight I can catch up some"
# And, its nothing but constant memorization. I feel like I'm watching my ex do anki decks in med school. Write 5 scripts on paper with no notes in an hour. Do 8 pages of trig with no notes or calculator in an hour. Sometimes same day.
# I seriously am considering leaving. This is ridiculouly brutal. I've literally felt my face on fire, I know what that smells like. I was also awake when they cut into my face by my left eye, so I know what that feels like too.       It's one of my favorite funny stories.
# This semester has made me cry twice.
# Probably will again this week.

class Solution:
    # Solution approach learned from NeetCode video tutorial
    # "Contains Duplicate" - accessed 2nd aug
    # https://neetcode.io/
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
    

# And its fucking up my 3.9 round up to 4 gpa.
# Ah. But, at least, if cornered in an alley at gunpoint and I had to do python without reference, and trig without reference: I stand a chance.