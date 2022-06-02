
print("Task 9")
print("Solution: [[['ee', 'ff'], ['cc', 'dd']]")
print("          []")
print("          [['ee', 'ff']]")
print("          [['cc', 'dd']]")

rental_obj = rental.rental()
rental_obj.add_user("aa", 11)
rental_obj.add_user("bb", 22)

rental_obj.add_rental_car("cc", "dd")
rental_obj.add_rental_car("ee", "ff")

result = rental_obj.rent_car("aa", "ff", 2019, 1, 3)
result = rental_obj.rent_car("aa", "ff", 2019, 1, 3)
result = rental_obj.rent_car("bb", "dd", 2019, 1, 3)


result = rental_obj.return_cars_rented()
print()
print("Data returned:")
print(result)
print()

result = rental_obj.return_cars_not_rented()
print()
print("Data returned:")
print(result)
print()

rental_obj.end_rental("bb", "dd", 2019, 2, 4)

result = rental_obj.return_cars_rented()
print()
print("Data returned:")
print(result)
print()

result = rental_obj.return_cars_not_rented()
print()
print("Data returned:")
print(result)
print()
