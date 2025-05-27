# class Soda:

#     def __init__(self, dobavka=None):
#         self.dobavka = dobavka

#     def show_my_drink(self):
#         if self.dobavka == None:
#             return "Sovorakan Gazirovka"
#         else:
#             return f'{self.dobavka}ov gazirovka'
        
# soda1 = Soda("Laym")
# soda2 = Soda()
# soda3 = Soda("Tandz")
# print(soda1.show_my_drink())
# print(soda2.show_my_drink())
# print(soda3.show_my_drink())



# class Triangle:

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def is_triangle(self):
#         try:
#             if self.a < 0 or self.b < 0 or self.c < 0:
#                 return "С отрицательными числами ничего не выйдет!"
#             elif self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
#                 return "Ура, можно построить треугольник!"
#             else:
#                 return "Жаль, но из этого треугольник не сделать"
#         except:
#             return "Нужно вводить только числа!"
        
# triangle1 = Triangle(6, 3, 4)
# print(triangle1.is_triangle())
# ----------------------------------------------------
# class KgToPounds:

#     def __init__(self, kg):
#         self.__kg = kg

#     def set_kg(self, new_kg):
#         self.__kg = new_kg

#     def get_kg(self):
#         return self.__kg
    
#     def to_pounds(self):
#         self.__kg = self.__kg * 2.2
    
# user1 = KgToPounds(1500)
# user1.to_pounds()
# print(user1.get_kg())
# ----------------------------------------------------
# class Words:

#     def __init__(self, word):
#         self.word = word

#     def max_ascii(self, new_word):
#         return self.word > new_word
    
#     def max_len(self, new_word):
#         return len(self.word) > len(new_word)
# ----------------------------------------------------
