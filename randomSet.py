# " !!! O(1) time for all functions !!! "

class RandomizedSet:

    def __init__(self):
        self.list = []
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        if val in self.dict: 
            return False
        else:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.dict: 
            last_element_val, last_element_idx = self.list[-1], self.dict[val]
            self.list[last_element_idx], self.dict[last_element_val] = last_element_val, last_element_idx
            # swap last element in array with the element to be removed
            
            del self.dict[val]
            self.list.pop()
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
