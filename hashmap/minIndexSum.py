class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = defaultdict(list)
        for ele in list1:
            if ele in list2:
                d[ele] = [list1.index(ele),list2.index(ele)]

        min_val = min(sum(v) for v in d.values()) # allow ties
        result = []
        for k, v in d.items():
            if sum(d[k]) == min_val:
                result.append(k)
        return result
