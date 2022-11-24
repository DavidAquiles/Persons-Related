from collections import deque
import search
class Node:
    def __init__(self,name,url,lst):
        self.name = name
        self.url = url
        self.lst = lst
        self.next = None
    
class Graph:
    def __init__(self,head):
        self.lst = head
        
        

def createNode(name, url, lst):
    p1 = Node(name, url, lst)
    return p1

"""def enqueueLst(conections):
    queue = deque()
    for i conections:

    return queue"""
        
def checkAnalized(Analized, Node):
    if Node in Analized:
        return checkAnalized(Analized,Node.next)
    else:
        return ((Node.name,Node.url),Node.lst)
    
    
def addToList(person,head):
    current = head
    while current.next is not None:
         current = current.next
    
    current.next = person
        
    return head


def searchName(p1,p2):
    str = p2.url
    current = p1
    while current != None:
        if str == current.url:
            return current.url
        for i in current.lst:
            if str == i[0][1]:
                return current.url               
        

    
def createGraph(tuple,p2):
    print("|"+tuple[0][0]+"|")
    analized = []
    p1 = createNode(tuple[0][0],tuple[0][1],tuple[1])
    if p2[0][1] in p1.lst:
        return (p1,True)
    newTuple = search.search(tuple)
    newPerson = createNode(newTuple[0][0],newTuple[0][1],newTuple[1])
    addToList(newPerson,p1)
    analized.append(p1)
    while len(analized) < 50:
        print("     |")
        print("     V")
        print("|"+newPerson.name+"|")
        if p2[0][1] in newPerson.lst:
            return (p1,True)
        else:
            toAnalize = checkAnalized(analized,p1)
            newTuple = search.search(toAnalize)
            while newTuple == "HTTP not finded":
                newTuple = search.search(toAnalize)
            for i in analized:
                if newTuple[0][0] == i.name:
                  newTuple = search.search(toAnalize)  
                  break
            newPerson = createNode(newTuple[0][0],newTuple[0][1],newTuple[1])
            addToList(newPerson,p1)
            analized.append(newPerson)
            
    
    return(p1,False)

def findPath(p1,p2,head):
    str = "->"+p2.name
    name = p2.name
    while name != p1.name:
        name = searchName(head,name)
        str = "->"+name+str
        
    return str[2:len(str)]
     
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    

    
    

    