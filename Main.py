# Think of at least five places in the world you would
# like to visit.

# Store the locations in a list. Make sure the list is not in
# alphabetical order.

seeing_the_world = [
    "Rome, Italy", "Edinburgh", "Scotland",
    "Kerry, Ireland", "Paris, France",
    "Cape Town, South Africa", "Tokyo, Japan",
    "London, England", "Amsterdam", "Greece",
    "Australia", "Thailand", "Germany", "Maui", "Tahiti"
]

# Print your list in its original order. Don't worry about
# printing the list neatly, just print it as a raw Python list.

print(seeing_the_world)

# Use sorted() to print your list in alphabetical order
# without modifying the actual list.

print(sorted(seeing_the_world))

# Show that your list is still in its original order by
# printing it.

print(seeing_the_world)

# Use sorted() to print your list in reverse alphabetical
# order without changing the original list.

print(sorted(seeing_the_world, reverse=True))

# Show that your list is still in its original order by
# printing it again.

print(seeing_the_world)

# Use reverse() to change the order of your list.
# Print the list to show that its order has changed

seeing_the_world.reverse()
print(seeing_the_world)

# Use reverse() to change the order of your list again.
# Print the list to show that it is back to its original
# order.

seeing_the_world.reverse()
print(seeing_the_world)

# Use sort() to change your list so it's stored in
# alphabetical order. Print the list to show its order has
# been changed.

seeing_the_world.sort()
print(seeing_the_world)

# Use sort() to change your list so it's stored in reverse
# alphabetical order. Print the list to show that its order
# has changed.

seeing_the_world.sort(reverse=True)
print(seeing_the_world)
