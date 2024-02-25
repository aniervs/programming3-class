class person:
    def __init__(self,name:str ,age:int) :
        self.name=name 
        self.age=age
persons=[] 
while (True):
    inp=input()
    if(inp=="exit"):
        break
    inp=inp.split(" ")
    if (inp[0]=='SET'):
        persons.append(person(inp[1],int(inp[2])))
    elif(inp[0]=='GET'):
        t=0
        for personn in persons :
            if (personn.name==inp[1]):
                print(personn.age)
                t=1
                break
        if t==0:
            print("there is no person with such name!")
    elif(inp[0]=='DELETE'):
        t=0
        for personn in persons :
            if (personn.name==inp[1]):
                persons.remove(personn)
                t=1
                break
        if t==0:
            print("there is no person with such name!")
    elif(inp[0]=='COUNT'):
        print(len(persons))
    elif (inp[0]=='GET_BY_AGE'):
        print(f"there are {len(persons)} of userse : ")
        for personn in persons :
            print(personn.name , personn.age) 
    else :
        print("Unknown request!")