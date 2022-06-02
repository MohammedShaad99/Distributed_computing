
print("Task 5 & 6")
print("Solution: []")
print("          ['aa', 'gg'], ['aa', 'gg'], ['bb', 'hh']")

rental_obj = rental.rental()

result = rental_obj.return_cars_not_rented()
print()
print("Data returned:")
print(result)
print()

rental_obj.add_rental_car("aa", "gg")
rental_obj.add_rental_car("aa", "gg")
rental_obj.add_rental_car("bb", "hh")
result = rental_obj.return_cars_not_rented()
print()
print("Data returned:")
print(result)
print()
