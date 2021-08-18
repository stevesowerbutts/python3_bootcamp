from csv import DictReader, DictWriter

# def find_user(first, last):
#     with open("users.csv") as file:
#         csv_reader = DictReader(file)
#         for line_no, line in enumerate(csv_reader, 1):
#             if line['First Name'] == first and line['Last Name'] == last:
#                 return line_no
#         return "{} {} not found.".format(first, last)
#
# find_user("Colt", "Steele") # 1
# find_user("Alan", "Turing") # 3
# find_user("Not", "Here") # 'Not Here not found.'

# with open('fighters.csv') as file:
# 	csv_reader = reader(file) #data never converted to list
# 	with open('screaming_fighters.csv', "w") as file:
# 		csv_writer = writer(file)
# 		for fighter in csv_reader:
# 			csv_writer.writerow([s.upper() for s in fighter])

# Exercise 102
# def update_users(old_first_name, old_last_name, new_first_name, new_last_name):
#     users = 0
#     with open('users.csv') as file:
#         csv_reader = DictReader(file)
#         all_users = list(csv_reader)
#
#     with open('new_users.csv', 'w') as new_file:
#         headers = ('First Name','Last Name')
#         csv_writer = DictWriter(new_file, fieldnames=headers)
#         csv_writer.writeheader()
#         for line_no, line in enumerate(all_users, 1):
#             if line['First Name'] == old_first_name and line['Last Name'] == old_last_name:
#                 csv_writer.writerow({
#         			"First Name": "blah",
#         			"Last Name": new_last_name
#         		})
#                 users += 1
#             else:
#                 csv_writer.writerow({
#         			"First Name": line['First Name'],
#         			"Last Name": line['Last Name']
#         		})
#         print("Users updated: {}".format(users))
#
# update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
# update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
# update_users("Not", "Here", "Still not", "Here") # Users updated: 0.


## Solution:
import csv

def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users updated: {}.".format(count)

update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
