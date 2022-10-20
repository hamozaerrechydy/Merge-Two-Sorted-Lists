def mergeTwoLists(list1, list2):
        print(s(m(list1, list2)))

def s(l): 
  NL = []
  for _ in range(len(l)):
     NL.append(min(l))
     l.remove(min(l))
  return NL

def m(a, b):
  t = [] 
  for x in a: 
    t.append(x) 

  for y in b: 
    t.append(y)

  return t

  
mergeTwoLists([1,3,2], [4,6,5])
