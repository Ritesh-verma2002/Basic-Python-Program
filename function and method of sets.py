# clear()
s={1,2,3,3,4,5}
print(s.clear())
#output:None



# copy()
s={1,2,3,3,4,5}
s1=s.copy()
print(s1)
#output: {1, 2, 3, 4, 5}



# difference()
s1={1, 2, 3, 4, 5}
s2={6, 8, 2, 4, 5}
print(s1.difference(s2))
# output={1, 3}




# difference_update()
s1={1, 2, 3, 4, 5}
s2={3,5,6,7,8,9,10}
s1.difference_update(s2)
print(s1)
#output= {1, 2, 4}




#discard()
s1={1, 2, 3, 4, 5}
s1.discard(2)
print(s1)
#output={1, 3, 4, 5}




# intersection()
s1={1, 2, 3, 4, 5}
s2={3,5,6,7,8,9,10}
print(s1.intersection(s2))
#output={3, 5}




# intersection_update()
s1={1, 2, 3, 4, 5}
s2={3,5,6,7,8,9,10}
s1.intersection_update(s2)
print(s1)
#output={3, 5}



# isdisjoint()
s1={1, 2, 3, 4, 5}
s2={3,5,6,7,8,9,10}
print(s1.isdisjoint(s2))
#output= False




# issubset()
s1={1, 2, 3, 4, 5}
s2={1,2,3,4,5,6,7,8,9,10}
print(s1.issubset(s2))
#output=True




# issuperset()
s1={1, 2, 3, 4, 5}
s2={1,2,3,4,5,6,7,8,9,10}
print(s2.issuperset(s1))
#output= True





# pop()
s1={1, 2, 3, 4, 5}
s2={3,5,6,7,8,9,10}
print(s1.pop(),s1)
#output=   1 {2, 3, 4, 5}





#remove()
s1={1, 2, 3, 4, 5}
s2={3,5,6,7,8,9,10}
s1.remove(2)
print(s1)
#  Output=   {1, 3, 4, 5}




#  symmetric_difference()
s1={1, 2, 3, 4, 5}
s2={3,5,6,7,8,9,10}
c=s1.symmetric_difference(s2)
print(c)
# output= {1, 2, 4, 6, 7, 8, 9, 10}




# union()
s1={1, 2, 3, 4, 5}
s2={3,5,6,7,8,9,10}
c=s1.union(s2)
print(c)
#output=  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}





#update()
s1={1, 2, 3, 4, 5}
s2={4,5,9,10}
s1.update(s2)
print(s1)
#output=  {1, 2, 3, 4, 5, 9, 10}





# all()
s1={1, 2, 3, 4, 5}
c=all(s1)
print(c)
#output= True





#any()
s1={1, 2, 3, 4, 5}
c=any(s1)
print(c)
#output= True





#enumerate()
s1="Ritesh verma"
print(list(enumerate(s1)))




#len()
s1={1, 2, 3, 4, 5}
c=len(s1)
print(c)
#output= 5





# max()
s1={1, 2, 3, 4, 5}
c=max(s1)
print(c)
#output=  5






# min()
s1={1, 2, 3, 4, 5}
c=min(s1)
print(c)
#output=  1




# sorted()
s1={1, 4, 3, 5, 2}
c=sorted(s1)
print(c)
#output=  {1,2,3,4,5}




# sum()
s1={1, 2, 3, 4, 5}
c=sum(s1)
print(c)
#output=   15







