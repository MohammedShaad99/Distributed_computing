
print("Task 3 & 4")
print("Solution: ['cc', 'dd'], ['ee', 'ff']")

rental_obj = rental.rental()
rental_obj.add_manufacturer("cc", "dd")
rental_obj.add_manufacturer("ee", "ff")
result = rental_obj.return_manufacturers()

print()
print("Data returned:")
print(result)
print()
