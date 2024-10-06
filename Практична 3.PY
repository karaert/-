Dict = {1:"2", 2:"20", 3:"33", 4:"4",5:"",6:"",7:"",8:"",9:"",10:""}

print(Dict)

Dict.update({2:10})
Dict.update({7:44})
Dict.pop(3)
Dict[4] = None

print(Dict)