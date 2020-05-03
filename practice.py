# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


""" 
The function Compute the "height" of a tree. Height is the  
number f nodes along the longest path from the root node  
down to the farthest leaf node. 
"""


def height(node):
    # Base Case : Tree is empty
    if node is None:
        return 0;

        # If tree is not empty then height = 1 + max of left
    # height and right heights
    return 1 + max(height(node.left), height(node.right))


# Function to get the diamtere of a binary tree
def diameter(root):
    # Base Case when tree is empty
    if root is None:
        return 0;

    # Get the height of left and right sub-trees
    lheight = height(root.left)
    rheight = height(root.right)

    # Get the diameter of left and irgh sub-trees
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    # Return max of the following tree:
    # 1) Diameter of left subtree
    # 2) Diameter of right subtree
    # 3) Height of left subtree + height of right subtree +1
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Diameter of given binary tree is %d" %(diameter(root)) )

#dijkstra : shortest path from soucre to all vertices

# import sys
#
#
# class Graph():
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
#
#     def printSolution(self, dist):
#         print('vertex distance from source')
#         for node in range(self.V):
#             print(node, dist[node])
#
#
#     def minDistance(self, dist, sptSet):
#         min = sys.maxint
#         for v in range(self.V):
#             if dist[v] < min and sptSet[v] == False:
#                 min = dist[v]
#                 min_index = v
#         return min_index
#
#     def dijkstra(self, src):
#         dist = [sys.maxint] * self.V
#         dist[src] = 0
#         sptSet = [False] * self.V
#         for cout in range(self.V):
#             u = self.minDistance(dist, sptSet)
#             sptSet[u] = True
#
#             for v in range(self.V):
#                 if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
#                     dist[v] = dist[u] + self.graph[u][v]
#
#         self.printSolution(dist)
#
#
#         return True
#
#
# # Driver program
# g = Graph(9)
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#            [4, 0, 8, 0, 0, 0, 0, 11, 0],
#            [0, 8, 0, 7, 0, 4, 0, 0, 2],
#            [0, 0, 7, 0, 9, 14, 0, 0, 0],
#            [0, 0, 0, 9, 0, 10, 0, 0, 0],
#            [0, 0, 4, 14, 10, 0, 2, 0, 0],
#            [0, 0, 0, 0, 0, 2, 0, 1, 6],
#            [8, 11, 0, 0, 0, 0, 1, 0, 7],
#            [0, 0, 2, 0, 0, 0, 6, 7, 0]
#            ];
#
# g.dijkstra(8);



# prolem: change value from 0<-->1 based on left and right adjacent
# from copy import deepcopy
# def cellCompete(states, days):
#     # WRITE YOUR CODE HERE
#     states_len = len(states)
#     for i in range(days):
#         new_states = deepcopy(states)
#         for j in range(len(states)):
#             if (j== 0 and states[j+1] ==0) or (j == (states_len-1) and states[states_len-2] == 0):
#                 new_states[j] = 0
#             elif( j== 0 and states[j+1] ==1) or (j == (states_len-1) and states[states_len-2] == 1):
#                 new_states[j] = 1
#             elif (0<j<(states_len-1) and states[j-1] == states[j+1]):
#                 new_states[j] =  0
#             else:
#                 new_states[j] = 1
#
#         states = new_states
#         print('after iteration %s, new states %s' %(i, states))
#
#     return states
#
#
# #states = [1, 0,0,0,0, 1, 0, 0]
# states = [1, 1,1,0,1,1,1,1]
# print (cellCompete(states, 3))

# class TrieNode(object):
#     def __init__(self, char):
#
#         self.children = []
#         self.word_finished = False
#         self.char = char
#         self.counter = 1
#
# def add(root, word):
#     node = root
#     for char in word:
#         found_in_child = False
#
#         for child in node.children:
#             if child.char == char:
#                 child.counter +=1
#                 node = child
#                 found_in_child = True
#                 break
#
#         if not found_in_child:
#             new_node = TrieNode(char)
#             node.children.append(new_node)
#             node = new_node
#     node.word_finished = True
#
#
# def find_prefix(root, prefix):
#     """
#     Check and return
#       1. If the prefix exsists in any of the words we added so far
#       2. If yes then how may words actually have the prefix
#     """
#     node = root
#     # If the root node has no children, then return False.
#     # Because it means we are trying to search in an empty trie
#     if not root.children:
#         return False, 0
#     for char in prefix:
#         char_not_found = True
#         # Search through all the children of the present `node`
#         for child in node.children:
#             if child.char == char:
#                 # We found the char existing in the child.
#                 char_not_found = False
#                 # Assign node as the child containing the char and break
#                 node = child
#                 break
#         # Return False anyway when we did not find a char.
#         if char_not_found:
#             return False, 0
#     # Well, we are here means we have found the prefix. Return true to indicate that
#     # And also the counter of the last node. This indicates how many words have this
#     # prefix
#     return True, node.counter
#
#
# if __name__ == "__main__":
#     root = TrieNode('*')
#     add(root, "hackathon")
#     add(root, 'hack')
#     import pdb; pdb.set_trace()
#
#     print(find_prefix(root, 'hac'))
#     print(find_prefix(root, 'hack'))
#     print(find_prefix(root, 'hackathon'))
#     print(find_prefix(root, 'ha'))
#     print(find_prefix(root, 'hammer'))


# substring for ending and closing with 1
# def ones_found(test_string):
#     n = len(test_string)
#     count = 0
#     final_list = []
#     for i in range(0, len(test_string)):
#         if test_string[i] == '1':
#             for k in range(i+1, n):
#                 if test_string[k]=='1':
#                     temp = test_string[i:k+1]
#                     final_list.append(temp)
#                     count = count + 1
#
#     return count, final_list
#
#
# sample = "00001000001010001000011"
#
# print(ones_found(sample))


#linked list implementation
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#
#     def reverse(self):
#         prev = None
#         current = self.head
#         while(current is not None):
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#         self.head = prev
#
#     def push(self, newdata):
#         new_node = Node(newdata)
#         new_node.next = self.head
#         self.head = new_node
#
#     def printList(self):
#         temp = self.head
#         while(temp):
#             print(temp.data)
#             temp = temp.next
#
# llist = Linkedlist()
# llist.push(10)
# llist.push(20)
# llist.push(30)
#
#
# llist.printList()
#
# llist.reverse()
#
# llist.printList()



# def reversestring(sname):
#
#     # for returning same in order
#     bn =''
#     for i in sname:
#         bn = i + bn
#     return bn
#
#     # reverse word in sentense
#     # bn = ''
#     # final_string = ''
#     # for i in sname:
#     #     if(i == ' ' ):
#     #         final_string = final_string + bn + ' '
#     #         bn = ''
#     #     else:
#     #         bn = i + bn
#     # return final_string + bn
#
# sname = 'abhishek ji ki barat'
# print(sname)
# print(reversestring(sname))


# class LittleMeta(type):
#     def __new__(cls, clsname, superclasses, attributedict):
#         print("clsname: ", clsname)
#         print("superclasses: ", superclasses)
#         print("attributedict: ", attributedict)
#         return type.__new__(cls, clsname, superclasses, attributedict)
#
# class S:
#     pass
# class A(S, metaclass=LittleMeta):
#     pass
# a = A()


# class Polynomial:
#     def __init__(self, *coefficients):
#         import pdb; pdb.set_trace()
#         self.coefficients = coefficients[::-1]
#     def __call__(self,x):
#         res = 0
#         import pdb; pdb.set_trace()
#         for index, coeff in enumerate(self.coefficients):
#             res+= coeff * x** index
#         return res
#     def __repr__(self):
#         return "Polynomial" + str(self.coefficients[::-1])
#
# p = Polynomial(4, 0, -4, 3, 0)
# print(p)




# method resoultion order
# class A:
#     def m(self):
#         print ('inside class A')
# class B(A):
#     def m(self):
#         print('inside class B')
# class C(A):
#     def m(self):
#         print('inside class C')
#
# class D(B,C):
#     def m(self):
#         print('inside class D')
#
# x = D()
# x.m()
# B.m(x)
# C.m(x)
# import pdb; pdb.set_trace()
# A.m(x)

# encapsulation : getter and setter replacement with property
# class Robot:
#
#     def __init__(self, name, build_year, lk=0.5, lp=0.5):
#         self.name = name
#         self.build_year = build_year
#         self.__potential_physical = lk
#         self.__potential_psychic = lp
#
#     @property
#     def condition(self):
#         # import pdb; pdb.set_trace() not able to get self instance here in pdb
#         s = self.__potential_physical + self.__potential_psychic
#         if s <= -1:
#             return "I feel miserable!"
#         elif s <= 0:
#             return "I feel bad!"
#         elif s <= 0.5:
#             return "Could be worse!"
#         elif s <= 1:
#             return "Seems to be okay!"
#         else:
#             return "Great!"
#
#
# if __name__ == "__main__":
#     x = Robot("Marvin", 1979, 0.2, 0.4)
#     y = Robot("Caliban", 1993, -0.4, 0.3)
#     print(x.condition)
#     print(y.condition)

#class methods and static methods
# class fraction(object):
#
#     def __init__(self, n, d):
#         self.numerator, self.denominator = fraction.reduce(n, d)
#
#     @staticmethod
#     def gcd(a, b):
#         while b != 0:
#             a, b = b, a % b
#             print (a, b)
#         import pdb;
#         pdb.set_trace()
#         return a
#
#     @classmethod
#     def reduce(cls, n1, n2):
#         import pdb; pdb.set_trace()
#         g = cls.gcd(n1, n2)
#         return (n1 // g, n2 // g)
#
#     def __str__(self):
#         return str(self.numerator) + '/' + str(self.denominator)
#
# x = fraction(15,27)
# print(x)

# static methods vs class methods difference
# class Birds:
#     name = 'this class is Birds'
#
#     @staticmethod
#     def about(cls):
#         print('this calss name is {}'.format(cls.name))
#
# class Duck(Birds):
#     name = 'duck name'
#
# class Crow(Birds):
#     name = 'crow name is CROW'
#
#
# b = Birds()
# b.about(Birds)
# print(b.name)
# d = Duck()
# print (d.name)
# d.about()
# c = Crow()
# c.about()



# class Robot():
#     __chamu__ = 'robot private variable'
#     def __init__(self, name, pname):
#         print(name + " has been created!")
#         self.name=name
#         self.__pname= pname
#
#     def __del__(self):
#         print(self.name + " says bye-bye!")
#
#
# if __name__ == "__main__":
#     x = Robot("Tik-Tok", 'ptik-tok')
#     y = Robot("Jenkins", 'pjenkins')
#     z = x
#     print("Deleting x")
#     del x
#     print("Deleting z")
#     del z
#     del y
# Robot.__dict__, x.__dict__, x.__class__.__dict__


# diffrence between __str__ and __repr__
# can get class object from repr object but for str it is not possible
# class Robot:
#
#     def __init__(self, name, build_year):
#         self.name = name
#         self.build_year = build_year
#
#     def __repr__(self):
#         return "Robot(\"" + self.name + "\"," + str(self.build_year) + ")"
#
#     def __str__(self):
#         return "Name: " + self.name + ", Build Year: " + str(self.build_year)
#
#
# if __name__ == "__main__":
#     x = Robot("Marvin", 1979)
#
#     x_repr = repr(x)
#     print(x_repr, type(x_repr))
#     new = eval(x_repr)
#     print(new)
#     print("Type of new:", type(new))


# def our_decorator(fun     c):
#     def function_wrapper(x):
#         print("Before calling " + func.__name__)
#         func(x)
#         print("After calling " + func.__name__)
#
#     return function_wrapper
#
#
# def foo(x):
#     print("Hi, foo has been called with " + str(x))
#
#
# print("We call foo before decoration:")
# foo("Hi")
#
# print("We now decorate foo with f:")
# foo = our_decorator(foo)
#
# print("We call foo after decoration:")
# foo(42)


#function inside function example
# def f(x):
#     #import pdb; pdb.set_trace()
#     def g(y):
#         return y + x + 3
#     return g
#
# nf1 = f(1)
# nf2 = f(3)
#
# print(nf1(1))
# print(nf2(1))
#


#medlife interview question
# def get_next_n_slots(week_config, current_time, n=10):
#     next_n_slots = []
#
#     for i in range(n):
#         for each in week_config:
#             for days in each:
#                 if days:
#                     if len(next_n_slots) >= n:
#                         break
#                     newdict = {'start_time': get_date_format(current_time, days['start_time']),
#                                'end_time': get_date_format(current_time, days['end_time'])}
#                     next_n_slots.append(newdict)
#             current_time = current_time + datetime.timedelta(days=1)
#
#     return next_n_slots
#
#
# def get_date_format(current_times, times):
#     dates = current_times.strftime('%Y-%m-%d')
#     if current_times.strftime('%H:%M:%S') > times :
#         current_times = current_times + datetime.timedelta(days=1)
#         dates = current_times.strftime('%Y-%m-%d')
#
#     finaldate = datetime.datetime.strptime(dates + ' ' + times, "%Y-%m-%d %H:%M")
#     expected_format = finaldate.strftime('%Y-%m-%d %H:%M:%S')
#     return expected_format
#
#
#
# INP_1 = [
#     [  # Monday
#         {"start_time": "06:00", "end_time": "06:30"},
#         {"start_time": "06:30", "end_time": "07:00"},
#         {"start_time": "07:00", "end_time": "07:30"},
#         {"start_time": "07:30", "end_time": "08:00"}
#     ]
#     , [  # Tuesday
#         # {"start_time": "06:00", "end_time": "06:30"},
#     ]
#     , [  # Wednesday
#         {"start_time": "06:00", "end_time": "06:30"},
#         {"start_time": "06:30", "end_time": "07:00"},
#         {"start_time": "07:00", "end_time": "07:30"},
#         {"start_time": "07:30", "end_time": "08:00"}
#     ], [  # Thursday
#         {"start_time": "09:00", "end_time": "09:30"},
#         {"start_time": "09:30", "end_time": "10:00"},
#         {"start_time": "10:00", "end_time": "10:30"},
#         {"start_time": "10:30", "end_time": "11:00"}
#     ], [  # Friday
#     ], [  # Saturday
#     ], [  # Sunday
#     ]
# ]
#
# import datetime
# time_of_run = datetime.datetime(2017, 1, 1, 20, 30)
# print (time_of_run)
# print(get_next_n_slots(INP_1, time_of_run, 14))


# INP_1 = [
#     [  # Monday
#         {"start_time": "06:00", "end_time": "06:30"},
#         {"start_time": "06:30", "end_time": "07:00"},
#         {"start_time": "07:00", "end_time": "07:30"},
#         {"start_time": "07:30", "end_time": "08:00"}
#     ], [  # Tuesday
#     ], [  # Wednesday
#         {"start_time": "06:00", "end_time": "06:30"},
#         {"start_time": "06:30", "end_time": "07:00"},
#         {"start_time": "07:00", "end_time": "07:30"},
#         {"start_time": "07:30", "end_time": "08:00"}
#     ], [  # Thursday
#         {"start_time": "09:00", "end_time": "09:30"},
#         {"start_time": "09:30", "end_time": "10:00"},
#         {"start_time": "10:00", "end_time": "10:30"},
#         {"start_time": "10:30", "end_time": "11:00"}
#     ], [  # Friday
#     ], [  # Saturday
#     ], [  # Sunday
#     ]
# ]
#
#
#
# OUT_1 = [
#     {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
#     {"start_time": "2017-01-02 06:30:00", "end_time": "2017-01-02 07:00:00"},
#     {"start_time": "2017-01-02 07:00:00", "end_time": "2017-01-02 07:30:00"},
#     {"start_time": "2017-01-02 07:30:00", "end_time": "2017-01-02 08:00:00"},
#     {"start_time": "2017-01-04 06:00:00", "end_time": "2017-01-04 06:30:00"},
#     {"start_time": "2017-01-04 06:30:00", "end_time": "2017-01-04 07:00:00"},
#     {"start_time": "2017-01-04 07:00:00", "end_time": "2017-01-04 07:30:00"},
#     {"start_time": "2017-01-04 07:30:00", "end_time": "2017-01-04 08:00:00"},
#     {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 09:30:00"},
#     {"start_time": "2017-01-05 09:30:00", "end_time": "2017-01-05 10:00:00"} ]
#
# INP_2 = [
# [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     []
# ]
# OUT_2 = []
#
# INP_3 = [
#     [  # Monday
#         {"start_time": "06:00", "end_time": "06:30"},
#         {"start_time": "06:30", "end_time": "07:00"},
#     ], [  # Tuesday
#         {"start_time": "06:00", "end_time": "06:30"},
#         {"start_time": "07:00", "end_time": "07:30"},
#         {"start_time": "07:30", "end_time": "07:45"}
#     ], [  # Wednesday
#     ], [  # Thursday
#         {"start_time": "09:00", "end_time": "10:00"}
#     ], [  # Friday
#     ], [  # Saturday
#     ], [  # Sunday
#     ]
# ]
#
# OUT_3 = [
#     {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
#     {"start_time": "2017-01-02 06:30:00", "end_time": "2017-01-02 07:00:00"},
#     {"start_time": "2017-01-03 06:00:00", "end_time": "2017-01-03 06:30:00"},
#     {"start_time": "2017-01-03 07:00:00", "end_time": "2017-01-03 07:30:00"},
#     {"start_time": "2017-01-03 07:30:00", "end_time": "2017-01-03 07:45:00"},
#     {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 10:00:00"},
#     {"start_time": "2017-01-09 06:00:00", "end_time": "2017-01-09 06:30:00"},
#     {"start_time": "2017-01-09 06:30:00", "end_time": "2017-01-09 07:00:00"},
#     {"start_time": "2017-01-10 06:00:00", "end_time": "2017-01-10 06:30:00"},
#     {"start_time": "2017-01-10 07:00:00", "end_time": "2017-01-10 07:30:00"} ]
#
# SAMPLE_INPUT_OUTPUTS = [
#      (INP_1, OUT_1),
#      (INP_2, OUT_2),
# (INP_3, OUT_3)
# ]
# import datetime
# time_of_run = datetime.datetime(2017, 1, 1, 20, 30)
#
# for ip, expected_output in SAMPLE_INPUT_OUTPUTS:
#     output = get_next_n_slots(ip, time_of_run)
#     import pdb; pdb.set_trace()
#     assert output == expected_output




# def bubble_sort(lst, k):
#     print(lst)
#     #import pdb; pdb.set_trace()
#     for i in range(len(lst)-1):
#         for j in range(i, len(lst)-1):
#             if lst[i] > lst[j]:
#                 temp = lst[i]
#                 lst[i] = lst[j]
#                 lst[j] = temp
#         print(lst)
#
#     print (lst)
#
# unsorted_list = [1, 23, 12, 9, 30, 2, 50]
# kth_list = 3
# #bubble_sort(unsorted_list, kth_list)
#
#
# def bubble(lst, k):
#     print(lst)
#     n = len(lst)
#     for i in range(k):
#         for j in range(0, n-i-1):
#             if lst[j] > lst[j+1]:
#                 temp = lst[j]
#                 lst[j] = lst[j+1]
#                 lst[j+1] = temp
#         print (lst)
#
# unsorted_list = [1, 23, 12, 9, 30, 2, 50]
# kth_list = 3
# bubble(unsorted_list, kth_list)





# def smallestelement(lst, k):
#     temp = []
#     #import pdb; pdb.set_trace()
#     for i in range(k):
#         temp.append(lst[i])
#         del lst[i]
#
#     print (temp, lst)
#
#     temp_min = temp[0]
#     for each in temp:
#         #import pdb; pdb.set_trace()
#
#         temp_min = each
#
#         for each in lst:
#             if temp_min > each:
#                 lst.append(temp_min)
#                 temp.append(each)
#                 lst.remove(each)
#                 temp.remove(temp_min)
#
#     print(temp, lst)
#
#
# unsorted_list = [1, 23, 12, 9, 30, 2, 50]
# kth_list = 3
# smallestelement(unsorted_list, kth_list)


#---------- merge sort implementation
# def merge_sort(unsorted_list):
#     if len(unsorted_list) <= 1:
#         return unsorted_list
# # Find the middle point and devide it
#     middle = len(unsorted_list) // 2
#     left_list = unsorted_list[:middle]
#     right_list = unsorted_list[middle:]
#
#     left_list = merge_sort(left_list)
#     right_list = merge_sort(right_list)
#     return list(merge(left_list, right_list))
#
# # Merge the sorted halves
#
# def merge(left_half,right_half):
#
#     res = []
#     while len(left_half) != 0 and len(right_half) != 0:
#         if left_half[0] < right_half[0]:
#             res.append(left_half[0])
#             left_half.remove(left_half[0])
#         else:
#             res.append(right_half[0])
#             right_half.remove(right_half[0])
#     if len(left_half) == 0:
#         res = res + right_half
#     else:
#         res = res + left_half
#     return res
#
# unsorted_list = [64, 34, 25, 12, 22, 11, 90]
#
# print(merge_sort(unsorted_list))
#
#  tree implementation , print and searching
# class Node:
#
#     def __init__(self, data):
#
#         self.left = None
#         self.right = None
#         self.data = data
#
# # Insert method to create nodes
#     def insert(self, data):
#
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data
# # findval method to compare the value with nodes
#     def findval(self, lkpval):
#         if lkpval < self.data:
#             if self.left is None:
#                 return str(lkpval)+" Not Found"
#             return self.left.findval(lkpval)
#         elif lkpval > self.data:
#             if self.right is None:
#                 return str(lkpval)+" Not Found"
#             return self.right.findval(lkpval)
#         else:
#             print(str(self.data) + ' is found')
# # Print the tree
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print( self.data),
#         if self.right:
#             self.right.PrintTree()
#
# root = Node(12)
# root.PrintTree()
# root.insert(6)
# root.insert(14)
# root.insert(3)
# print(root.findval(7))
# print(root.findval(14))
# root.PrintTree()
#


#maximum water accumulation problem statement
#class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         left, right = 0, len(height) - 1
#         res = maxleft = maxright = 0
#         while left <= right:
#             if height[left] <= height[right]:
#                 if height[left] >= maxleft:
#                     maxleft = height[left]
#                 else:
#                     res += maxleft - height[left]
#                 left += 1
#             else:
#                 if height[right] >= maxright:
#                     maxright = height[right]
#                 else:
#                     res += maxright - height[right]
#                 right -= 1
#         return res
#
#
# s = Solution()
# arr = [3, 0, 0, 2, 0, 4]
# n = len(arr)
# print("Maximum water that can be accumulated is", s.trap(arr))

# ----------------find two sum is thare
# class TwoSum:

#     @staticmethod
#     def find_two_sum(numbers, target_sum):
#         """
#         :param numbers: (list of ints) The list of numbers.
#         :param target_sum: (int) The required target sum.
#         :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
#         """
#         match = 0
#         result = []
#         for i in range(len(numbers)-1):
#             for j in range(i+1, len(numbers)):
#                 if (numbers[i] + numbers[j] == target_sum):
#                     match += 1

#                     lst = []
#                     lst.append(i)
#                     lst.append(j)
#                     l = tuple(lst)


#         if match == 0:
#             return (-1,-1)
#         else:
#             return l

# print(TwoSum.find_two_sum([1, 3, 5, 7, 9], 12))

# -------------adding two dict
# x  = {'a':1,'b':2}
# y  = {'b':3,'c':5}
# z = dict(x, **y)
# print z
# ----------------------- invert array
# m = [[1,2],[3,4],[5,6]]

# for row in m :
#     print(row)
# rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
# print("\n")
# for row in rez:
#     print(row)

# ---------------------------
# import multiprocessing

# print("Number of cpu : ", multiprocessing.cpu_count())
# ------------------------------
# generator example
# def multiplyByFive(*kwargs):
#    for i in kwargs:
#        yield i * 5

# a = multiplyByFive(4, 5, 6, 8)

# # showing the values
# for i in a:
#    print(i)
# -----------------------
# import this
# -----------------------------------
# def nos(n):
#     if n>0:
#         nos(n-1)
#         print n


# nos(100)


# -----------------------------------------
# import commands
# import subprocess
# import os
# import sys
# import git


# # repo = git.Repo('C:\Users\mmt6237\GoibiboPythonAutomation' )
# # xt = repo.git.log(p=True)

# # g = git.Git("C:\Users\mmt6237\GoibiboPythonAutomation")
# # loginfo = g.log('--since=2017-09-01','--author=Abhishek6237','--pretty=tformat:','--numstat')
# # print loginfo

# def gitlogjson(fromdate,todate,author):
#     GIT_COMMIT_FIELDS = ['id', 'author_name', 'author_email', 'date', 'message']
#     GIT_LOG_FORMAT = ['%H', '%an', '%ae', '%ad', '%s']

#     pr = subprocess.Popen( 'git log --after="2017-10-26" --pretty=format:" \"%h\": {%n  \"commit\" : \"%H\" , %n  \"author\" : \"%an\" ,%n  \"date\": \"%ai\",%n  \"message\": \"%s\"%n},', cwd =  'C:\Users\mmt6237\GoibiboPythonAutomation' , shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
#     (log, _) = pr.communicate()
#     import pdb; pdb.set_trace()
#     print "log::: " + str(log)
#     log = log.strip('\n\x1e').split("\x1e")
#     log = [row.strip().split("\x1f") for row in log]
#     log = [dict(zip(GIT_COMMIT_FIELDS, row)) for row in log]


#     print log

# gitlogjson('2017-10-26','2017-11-23','Abhishek Gupta')


# (out, error) = pr.communicate()

# print "Error : " + str(error)
# print "out : " + str(out)

# ----------------------------------------------------------------------------------
# def permutation(lst):

#     # If lst is empty then there are no permutations
#     if len(lst) == 0:
#         return []

#     # If there is only one element in lst then, only
#     # one permuatation is possible
#     if len(lst) == 1:
#         return [lst]

#     # Find the permutations for lst if there are
#     # more than 1 characters

#     l = [] # empty list that will store current permutation

#     # Iterate the input(lst) and calculate the permutation
#     for i in range(len(lst)):
#        m = lst[i]

#        # Extract lst[i] or m from the list.  remLst is
#        # remaining list
#        import pdb;pdb.set_trace()
#        remLst = lst[:i] + lst[i+1:]

#        # Generating all permutations where m is first
#        # element
#        for p in permutation(remLst):
#            l.append([m] + p)
#     return l


# # Driver program to test above function
# data = list('nikl')
# for p in permutation(data):
#     print p


# --------------------- QuickSort Recursion----------------------

# def partition(arr,low,high):
#     i = ( low-1 )         # index of smaller element
#     pivot = arr[high]     # pivot

#     import pdb;pdb.set_trace()
#     for j in range(low , high):

#         # If current element is smaller than or
#         # equal to pivot
#         if   arr[j] <= pivot:

#             # increment index of smaller element
#             i = i+1
#             arr[i],arr[j] = arr[j],arr[i]

#     arr[i+1],arr[high] = arr[high],arr[i+1]
#     return ( i+1 )


# def quickSort(arr,low,high):
#     if low < high:

#         # pi is partitioning index, arr[p] is now
#         # at right place
#         pi = partition(arr,low,high)

#         # Separately sort elements before
#         # partition and after partition
#         quickSort(arr, low, pi-1)
#         quickSort(arr, pi+1, high)


# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr,0,n-1)
# print ("Sorted array is:")
# for i in range(n):
#     print ("%d" %arr[i])


# ----------------------------selection sort-----------------
# import sys
# A = [64, 25, 12, 22, 11]

# # Traverse through all array elements
# for i in range(len(A)-1):

#     # Find the minimum element in remaining
#     # unsorted array
#     min_idx = i
#     for j in range(i+1, len(A)):
#         if A[min_idx] > A[j]:
#             min_idx = j

#     # Swap the found minimum element with
#     # the first element
#     A[i], A[min_idx] = A[min_idx], A[i]

# # Driver code to test above
# print ("Sorted array")
# for i in range(len(A)):
#     print("%d" %A[i])

# --------------------------------

# def trippletcode(b,n):
#     print (n)
#     l =[]
#     a= []
#     count = 0

#     for i in range(n):
#         a.append(b[i]*b[i])

#     a.sort()
#     import pdb; pdb.set_trace()
#     for i in range(n-1,1,-1):
#         k=i-1
#         j=0
#         while (j<k):
#             if (a[j] + a[k] == a[i]):
#                 count +=1
#                 #l.append(a[i])

#             else:
#                 if(a[j]+ a[k] < a[i]):
#                     j +=1
#                 else:
#                     k-=1
#     if count>0 :
#         return True
#     else :
#         return False


# inputarr = []
# import pdb; pdb.set_trace()
# for i in range(6):
#     inputarr.append(i)

# lenght = len(inputarr)
# res = trippletcode(inputarr,lenght)

# print ('::::: tripplet result is:::: '+ str(inputarr)  + str(res) )


# ---------------------------------longest binary match of given number-----------------

# def longestcommon(n,m):
#     print n,m
#     print dectobin(n), dectobin(m)
#     str1 = str(dectobin(n))
#     str2 = str(dectobin(m))

#     length = len(str1)
#     l = length
#     mx = 0
#     while length>0:
#         for i in range(0, l-length+1):
#             #import pdb; pdb.set_trace()
#             #print str1[i:i+length]
#             temp = str1[i:i+length]
#             tlen = len(temp)
#             print temp
#             import pdb; pdb.set_trace()
#             if (tlen > mx and str2.find(temp) != -1):
#                 mx= tlen
#                 res = temp

#             i +=1
#         length-=1

#     if res== '':
#         return False
#     else:
#         return res
# def dectobin(n):
#     if n==0:
#         return ''
#     else:
#         return dectobin(n/2) + str(n%2)


# n= 8
# m= 13
# print longestcommon(n,m)


# ----------------------------------------------
# import sys
# import numpy as np

# # override default recursion limit
# sys.setrecursionlimit(1000000000)


# class NQueens:

#     def __init__(self, size_of_board):
#         self.size = size_of_board
#         self.columns = [] * self.size
#         self.num_of_places = 0
#         self.num_of_backtracks = 0

#     def place(self, startRow=0):
#         import pdb; pdb.set_trace()
#         """ Backtracking algorithm to recursively place queens on the board
#             args:
#                 startRow: the row which it attempts to begin placing the queen
#             returns:
#                 list representing a solution
#         """
#         # if every column has a queen, we have a solution
#         if len(self.columns) == self.size:
#             print('Solution found! The board size was: ' + str(self.size))
#             print(str(self.num_of_places) + ' total places were made.')
#             print(str(self.num_of_backtracks) + ' total backtracks were executed.')
#             print(self.columns)
#             return self.columns

#         # otherwise search for a safe queen location
#         else:
#             for row in range(startRow, self.size):
#                 import pdb; pdb.set_trace()
#                 # if a safe location in this column exists
#                 if self.isSafe(len(self.columns), row) is True:
#                     # place a queen at the location
#                     self.columns.append(row)
#                     self.num_of_places += 1
#                     # recursively call place() on the next column
#                     return self.place()

#                 # if not possible, reset to last state and try to place queen
#             else:
#                 # grab the last row to backtrack from
#                 lastRow = self.columns.pop()
#                 self.num_of_backtracks += 1
#                 # recursively call place() from the last known good position, incrementing to the next row
#                 return self.place(startRow=lastRow + 1)

#     def isSafe(self, col, row):
#         """Determines if a move is safe.
#         args:
#             col: column of desired placement
#             row: row of desired placement
#             self.columns: list of queens presently on the board
#         returns:
#             True if safe, False otherwise
#         """
#         # check for threats from each queen currently on board
#         for threatRow in self.columns:
#             # for readability
#             import pdb; pdb.set_trace()
#             threatCol = self.columns.index(threatRow)
#             # check for horizontal/vertical threats
#             if row == threatRow or col == self.columns.index(threatRow):
#                 return False
#             # check for diagonal threats
#             elif threatRow + threatCol == row + col or threatRow - threatCol == row - col:
#                 return False
#         # if we got here, no threats are present and it's safe to place the queen at the (col, row)
#         import pdb; pdb.set_trace()
#         return True

# # set the size of the board
# n = 4
# # instantiate the board and call the backtracking algorithm
# #import pdb; pdb.set_trace()
# queens = NQueens(n)
# queens.place(0)

# # convert board to numpy array for pretty printing
# board = np.array([[' '] * n] * n)
# for queen in queens.columns:
#     board[queens.columns.index(queen), queen] = 'Q'

# print board


# ----------------------------
# complexity O(nLogn)
# a= [5,6,-6,0,0,-2]
# print a
# if len(a)>1:
#     b= sorted(a, reverse=True)
#     print b
#     if (b[0] > 0 and b[len(b)-1] > 0):
#         max = a[0]*a[1]
#     else:
#         max = (b[0]*b[1])  if (b[0]*b[1]) > (b[len(b)-1]*b[len(b)-2]) else (b[len(b)-1]*b[len(b)-2] )
#     print max
# else:
#     print 'no data for comparison'


# ---------------
# def verifypalindrome(s):
#     print s
#     s= s.lower()
#     l=0
#     import pdb; pdb.set_trace()
#     h= len(s)-1
#     while(l<=h):
#         if (not (s[l]>='a' and s[l]<='z')):
#             l+=1
#         elif (not (s[h]>='a' and s[h]<='z')):
#             h-=1
#         elif(s[l]==s[h]):
#             l +=1
#             h -=1
#         else:
#             return False
#     return True
# s = 'Too hot to hoot'
# if verifypalindrome(s):
#     print (s + ':::is palindrom')
# else:
#     print (s + '::is not palindrome')


# ------------------------------------
# Python program to calculate number of times
# the pattern occured in given string

# Returns count of occurrences of "1(0+)1"


# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# # Replace below path with the absolute path
# # to chromedriver in your computer
# driver = webdriver.Chrome('C:\\Users\\mmt6237\\gothor\\chromedriver')

# driver.get("https://web.whatsapp.com/")
# wait = WebDriverWait(driver, 600)

# # Replace 'Friend's Name' with the name of your friend
# # or the name of a group
# target = '"Airtel Anku"'

# import pdb; pdb.set_trace()
# # Replace the below string with your own message
# string = "Message sent using Python!!!"

# x_arg = '//span[contains(@title,' + target + ')]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))
# group_title.click()
# inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
# input_box = wait.until(EC.presence_of_element_located((
#     By.XPATH, inp_xpath)))
# for i in range(100):
#     input_box.send_keys(string + Keys.ENTER)
#     time.sleep(1)


# ----------------------------------

# import fbchat
# from getpass import getpass
# username = str(raw_input("Username: "))
# client = fbchat.Client(username, getpass())
# #no_of_friends = int(raw_input("Number of friends: "))
# friendlist = ['Jitendra Dixit','Mohit Gupta','Gaurav Yadav','Pratik']
# k=1
# for each in friendlist:
#     #name = str(raw_input("Name: "))
#     name = each
#     #import pdb; pdb.set_trace()
#     friends = client.searchForUsers(name, limit=1)  # return a list of names
#     friend = friends[0]
#     #msg = str(raw_input("Message: "))
#     msg = 'good morning!!'+ str(name) + ', this is an automatic chat'
#     sent = client.sendMessage(msg + str(k), friend.uid)
#     k +=1
#     if sent:
#         print("Message sent successfully!")

# ----------------------------------------------

# def frequencyletter(stmt):
#     count = {}
#     for each in stmt:
#         if each in count:
#             count[each] +=1
#         else:
#             count[each] = 1

#     max = 0
#     for each in count:
#     	 if max > count[each]:
#     	 	print each
#     	 else:
#     	 	max = count[each]
#     	 	print each ,count[each]
#     print max

#     for each in count:
#     	number = ord(count[each])
#     	print number
#     	#output.append(number)

#     return count

# frequencyletter(100034343)


# [60 50 30] ----------------------------------------------------

# def maxprofit(lst):
#     dic = {}
#     i=0
#     for each in lst:
#         dic['day' + str(i)] = int(each)
#         i +=1
#     maximum=-1
#     largest = []
#     for num in dic.values():
#         largest.append(num)
#     sl =  sorted(largest, reverse=True)
#     max_profit = sl[0] -sl[1]
#     print max_profit


# string_input = raw_input('Enter Stock price list:::')
# input_list = string_input.split()
# print maxprofit(input_list)
