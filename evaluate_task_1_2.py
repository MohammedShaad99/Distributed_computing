
print("Task 1 & 2")
print("Solution: ['aa', 11], ['bb', 22]")

rental_obj = rental.rental()
rental_obj.add_user("aa", 11)
rental_obj.add_user("bb", 22)
result = rental_obj.return_users()

print()
print("Data returned:")
print(result)
print()
