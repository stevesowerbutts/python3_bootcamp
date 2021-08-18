# lists

Lists can be of any typ

Create list of nums using range:
  nums = list(range(1,100))

List methods


list.append(x) - append a single item x

list.extend([x,y,z]) - extends the list by x, y, z items

list.insert(index_in_list, item)

list.clear() - empty the list

list.pop() - removes last item by default
list.pop(x) - removes item at position x, returns that item for use in another variable etc if needed.
  popped = list.pop(x)

list.remove(item) - if item is in the list, it removes item (only removes a single occurence of the item)

friend.capitalize() - capitalize the first letter

# Slices

Start with []
Ways to select from inside lists of strings
eg.
[1] will select from index 1 in the list.
[::-1] will reverse a list or sting

`['Ellie', 'Tim', 'Matt'][::-1] == ['Matt', 'Tim', 'Ellie']`
`"amazing"[::-1] == 'gnizama'`
