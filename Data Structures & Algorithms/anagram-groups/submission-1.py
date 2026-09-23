class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            words = "".join(sorted(word))
            if words not in hashmap:
                hashmap[words] = []
            hashmap[words].append(word)

        return list(hashmap.values())