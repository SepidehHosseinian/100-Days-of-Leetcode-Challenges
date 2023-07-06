class MyHashSet:

    def __init__(self):
        self.key=[]
      
    def add(self, key: int) -> None:
        if key not in self.key:
            self.key.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.key:
            self.key.remove(key)
           
        
    
    def contains(self, key: int) -> bool:
        
        return  key in self.key
#705
        
            
          
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)