
print("Task 12")
print("Solution: ['ff']")
print("Solution: []")

rental_obj = rental.rental()
rental_obj.add_user("aa", 11)
rental_obj.add_user("bb", 22)

rental_obj.add_rental_car("cc", "dd")
rental_obj.add_rental_car("ee", "ff")

result = rental_obj.rent_car("aa", "ff", 2019, 1, 3)
rental_obj.end_rental("aa", "ff", 2019, 2, 4)

result = rental_obj.rent_car("bb", "dd", 2019, 1, 3)
rental_obj.end_rental("bb", "dd", 2019, 2, 4)

result = rental_obj.user_rental_date("aa", 2019, 1, 3, 2019, 3, 4)
print()
print("Data returned:")
print(result)
print()

result = rental_obj.user_rental_date("bb", 2019, 1, 3, 2019, 1, 4)
print()
print("Data returned:")
print(result)
print()
