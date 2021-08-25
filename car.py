# class Car:
#     def __init__(self, input_name):
#         self.year = 2003
#         self.color = "pink"
#         self.name = input_name
#
#     def update_name(self, new_name):
#         print("old name = ", first.name)
#         first.name = new_name
#         print("after update ", first.name)
#
#     def print_members(self):
#         print("year = ", self.year, " color= ", self.color, " name = ", self.name)
#
#
# car_list = []
# kostya_car = Car("Kostya")
# car_list.append(kostya_car)
# vova_car = Car("VOVA")
# car_list.append(vova_car)
#
# print("len = ", len(car_list))
#
# for item in car_list:
#     print("name is ", item.name)


class Car:
    def __init__(self, input_name):
        self.year = 2003
        self.color = "pink"
        self.name = input_name

    def update_name(self, new_name):
        print("old name = ", first.name)
        first.name = new_name
        print("after update ", first.name)


first = Car("Kostya")
first.update_name("roma")
print()
first.update_name("tanya")