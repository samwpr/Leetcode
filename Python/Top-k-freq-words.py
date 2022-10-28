#Top K Frequent Words

import heapq

class Solution:
    def topKFreq(self, words: list[str], k: int) -> list[str]:
        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

        heap =[(-freq, word) for word, freq in word_freq.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]

obj = Solution()
print(obj.topKFreq(["i","love","leetcode","i","love","coding"], k=2))
#Output: ["i","love"]

print(obj.topKFreq(["the","day","is","sunny","the","the","the","sunny","is","is"], k=4))
#Output: ["the","is","sunny","day"]

        
