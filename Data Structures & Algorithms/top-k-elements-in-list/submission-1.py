class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        # finding the most frequent elements based on k
        # loop through using hashmap and grab the counts of each num


        elements = {}
        finalList = []


        for i in nums:
            elements[i] = elements.get(i, 0) + 1
        
        for i in range(k):
            max_key = max(elements, key=elements.get) 
            finalList.append(max_key)
            del elements[max_key]
            
        return finalList