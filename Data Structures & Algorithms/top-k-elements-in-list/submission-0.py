class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}

        for i in nums:
            key = i
            if key in hashmap:
                hashmap[key] += 1
            else:
                hashmap[key] = 1 

        sorted_list = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        sor = []
        for s in sorted_list[:k]:
            sor.append(s[0])
        return sor