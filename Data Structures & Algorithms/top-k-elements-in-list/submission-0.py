class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for x in nums:
            if x not in count:
                count[x] = 0
            count[x] = count[x] + 1

        ordered =sorted(count,key=count.get,reverse=True)

        return ordered[:k]            
            