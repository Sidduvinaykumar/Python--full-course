
# Tech=[] # empty list
# print(type(Tech))
""" Indexin and access elements with index
 """
# Mixted_list=[1,2.2,'vizag',True,[1,2,3,'subscribe']]
# print(Mixted_list[4])
# print(Mixted_list[4][3])
# print(Mixted_list[-1][-3])


# Mango=[22,12,32,22,42,22,52,22,52,3,6]
# print(Mango[0:3])
# print(Mango[::-1])# it will reverse the total string from negitive side
# print(Mango[5:])
# print( Mango[1:10:4])
# print(Mango[start:stop]) #stop =n-1
# print(Mango[start:stop:skip]) #skip =n-1


""" List Methods  """
""" Syntex """
# variablename.method()
#  
# anusri=[33,11,33,4,3,54,54,4]
# anusri.append([15,'hello'])

# anusri.append(64)#it adds the elements at last of the present list
# print (anusri)

# anusri.extend([1111,3,4,6,7,8])#it adds elements at the end of the list like elements 
# print(anusri)

# v=anusri.copy()
# anusri.append(22) #it will not add elements after copy method used
# print(v)

# anusri.clear()# it will clear the all list
# print(anusri)


# print(anusri.count(33))#it will count the repeted once 

# print(len(anusri))#it counts the no of elements listed in list

# print(anusri.index(4))#it counts the index of the element listed in list
# anusri=[33,44,44]
# anusri.insert(0,'python') #it insert the element with the specified index
# print(anusri)

# anusri[0]='raghu'
# print(anusri)

# anusri=[33,11,3,4,3,54,54,4]
# # anusri.pop(0)it removes the element with help of index
# anusri.remove(4)it removes the element with help of element
# print(anusri)

# anusri=[33,11,3,54,4]
# anusri.reverse()
# print(anusri)



# anusri.sort(reverse=True)high to low &low to high shorting

# anusri.insert(0,'Hell8o')
# print(anusri)


# Finds the  element and print the len

a_list = ['aple', 'orange', 'aple', 'banana', 'grape', 'aple']

for i in range(len(a_list)):#6 after range 5
    if a_list[i] == 'aple': # i=0 a_list[0]
        print(i)
3






# remove duplicates in list
# ints_list = [1, 2, 3, 4, 3, 2]
# temp = [] # 1 2 3 4 
# for x in ints_list:
#     if x not in temp:# 
#         temp.append(x)
# print(temp)



