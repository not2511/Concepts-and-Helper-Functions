class Hashtable:
    def __init__(self,size=7):
        self.data_map=[None]*size
        
    def __hash(self,key):
        my_hash=0
        for letter in key:
            my_hash=(my_hash+ord(letter)*23)%len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,":",val)
            
    def set_item(self,key,value):
        index=self.__hash(key)
        if self.data_map[index]==None:
            self.data_map[index]=[]
        self.data_map[index].append([key,value])
        
    def  get_item(self,key):
        index=self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
        return None
    
    def item_in_common(self,list1,list2):
        my_dict={}
        for i in list1:
            my_dict[i]=True
        for j in list2:
            if j in my_dict:
                return True
        return False