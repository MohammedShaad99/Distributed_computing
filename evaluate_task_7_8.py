
print("Task 7 & 8")
print("Solution: []")
print("          1")
print("          0")
print("          [['ee', ff']")

rental_obj = rental.rental()
rental_obj.add_user("aa", 11)
rental_obj.add_user("bb", 22)

rental_obj.add_rental_car("cc", "dd")
rental_obj.add_rental_car("cc", "dd")
rental_obj.add_rental_car("ee", "ff")

result = rental_obj.return_cars_rented()
print()
print("Data returned:")
print(result)
print()

result = rental_obj.rent_car("aa", "ff", 2019, 1, 3)
print()
print("Data returned:")
print(result)
print()

result = rental_obj.rent_car("aa", "ff", 2019, 1, 3)
print()
print("Data returned:")
print(result)
print()

result = rental_obj.return_cars_rented()
print()
print("Data returned:")
print(result)
print()
