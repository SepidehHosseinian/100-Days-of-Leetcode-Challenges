class MyHashMap:

    def __init__(self):
        self.map=dict()
        

    def put(self, key: int, value: int) -> None:
        self.map[key]= value
        

    def get(self, key: int) -> int:
        if  key in self.map.keys():
            return self.map.get(key)
        else: return -1
        

    def remove(self, key: int) -> None:
         if key in self.map.keys():
            del self.map[key]
    #706        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)