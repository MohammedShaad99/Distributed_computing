
print("Task 11")
print("Solution: [['aa', 11]]")


rental_obj = rental.rental()
rental_obj.add_user("aa", 11)
rental_obj.add_user("bb", 22)

rental_obj.add_rental_car("cc", "dd")
rental_obj.add_rental_car("ee", "ff")

result = rental_obj.rent_car("aa", "ff", 2019, 1, 3)
rental_obj.end_rental("aa", "ff", 2019, 2, 4)

print("The method delete_user should return a value of 1...")
rental_obj.delete_user("aa")
rental_obj.delete_user("bb")

# Add check for the following
#The method delete_user should return a value of 1 if the user in question was successfully deleted. Otherwise, the method should return a value of 0.

result = rental_obj.return_users()

print()
print("Data returned:")
print(result)
print()
