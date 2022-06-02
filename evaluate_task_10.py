
print("Task 10")
print("Solution: [['ee', 'ff']]")
print("Solution: []")

rental_obj = rental.rental()
rental_obj.add_user("aa", 11)
rental_obj.add_user("bb", 22)

rental_obj.add_rental_car("cc", "dd")
rental_obj.add_rental_car("ee", "ff")

result = rental_obj.rent_car("aa", "ff", 2019, 1, 3)
rental_obj.delete_car("ff")
rental_obj.delete_car("dd")

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
