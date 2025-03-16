# this is optional if want to call funcs directly like:
# from my_package import add
# print(add(3, 2))

# without this it would look like:
# from my_package import module
# print(module.add(10, 5))

from .module import add, subtract, multiply, divide
