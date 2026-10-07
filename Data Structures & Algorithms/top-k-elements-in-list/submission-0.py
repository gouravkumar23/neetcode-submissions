from typing import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq= Counter(nums)
        print(freq.most_common(k))
        return [i[0] for i in freq.most_common(k)]