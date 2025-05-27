# class Human:

#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     def get_age(self): # Publie
#         return self.__age # Private

#     def set_age(self, new_age):
#         if new_age > 0:
#             self.__age = new_age

#     def __str__(self):
#         return f'{self.name}, {self.__age}'

# h1 = Human('Gor', 20)
# h1.set_age(23)
# print(h1.get_age())
# h1.__age -= 800
# print(h1)


# h1 = Human('Gor', 20)
# h1._Human__age -= 780
# print(h1.__dict__)
# print(h1._Human__age)
# --------------------------------------------------------------------
# from abc import ABC, abstractmethod


# class Transport(ABC):

#     @abstractmethod
#     def delivery(self):
#         pass
    
#     @abstractmethod
#     def pay(self):
#         pass

# class Truck(Transport):

#     def drive(self):
#         return "Truck (drive method)"
    
#     def drift(self):
#         return "Truck (drift method)"
    
#     def delivery(self):
#         return "Truck (delivery method)"
    
# class Moped(Transport):

#     def drive(self):
#         return "Moped (drive mthod)"
    
#     def delivery(self):
#         return "Moped (delivery method)"
    

# x = Truck()
# print(x.drift())
# --------------------------------------------------------------------
# import math

# class PaginationHelper:
    
#     # The constructor takes in an array of items and an integer indicating
#     # how many items fit within a single page
#     def __init__(self, collection, items_per_page):
#         self.collection = collection
#         self.items_per_page = items_per_page
    
#     # returns the number of items within the entire collection
#     def item_count(self):
#         return len(self.collection)
    
#     # returns the number of pages
#     def page_count(self):
#         return math.ceil(len(self.collection) / self.items_per_page)
    
#     # returns the number of items on the given page. page_index is zero based
#     # this method should return -1 for page_index values that are out of range
#     def page_item_count(self, page_index):
#         if page_index < 0 or page_index >= self.page_count():
#             return -1
#         elif page_index == self.page_count() - 1 and len(self.collection) % self.items_per_page != 0:
#             return len(self.collection) % self.items_per_page
#         else:
#             return self.items_per_page
#     # determines what page an item at the given index is on. Zero based indexes.
#     # this method should return -1 for item_index values that are out of range
#     def page_index(self, item_index):
#         return item_index // self.items_per_page


# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# helper.page_count() # should == 2
# helper.item_count() # should == 6
# helper.page_item_count(0) # should == 4
# helper.page_item_count(1) # last page - should == 2
# helper.page_item_count(2) # should == -1 since the page is invalid

# # page_index takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# helper.page_index(2) # should == 0
# helper.page_index(20) # should == -1
# helper.page_index(-10) # should == -1 because negative indexes are invalid


# ---------------------------------------------------------------------
# class CheckName:

#     name_dict = {
#         1:'ajs',
#         2:'bkt',
#         3:'clu',
#         4:'dmv',
#         5:'enw',
#         6:'fox',
#         7:'gpy',
#         8:'hqz',
#         9:'ir'
#     }

#     def __init__(self, name):
#         self.name = name.lower()

#     def check_name(self):
#         summ = 0
#         for i in self.name:
#             for j in CheckName.name_dict:
#                 if i in CheckName.name_dict[j]:
#                     summ += j
#         if summ ** 0.5 >= 5:
#             return "yes"
#         else:
#             return "no"
        
# name1 = CheckName("Miqayel")
# name2 = CheckName("Gor")
# name3 = CheckName("Ani")
# name4 = CheckName("Lusine")
# print(name1.check_name())
# print(name2.check_name())
# print(name3.check_name())
# print(name4.check_name())
# ---------------------------------------------------------------------
