# class base:
#     def func1(self):
#         print(" i m in function 1")
#     def func2(self):
#         print("i m in function 2")
class three:
    def func3(self):
        print("i m in class three")
class two(three):
    def func2(self):
        print("i m in class two")
class one(two):
    def func1(self):
        print("i m in class one")
o1=one()
o1.func1()
o1.func2()
o1.func3()