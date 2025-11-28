"""
Comparison of Tuple, Set, and List data structures in Python
Demonstrates key differences: mutability, ordering, duplicates, and operations
"""

# Input values
a, b, c, d = 10, 20, 30, 20

print("=" * 60)
print("TUPLE - Immutable, Ordered, Allows Duplicates")
print("=" * 60)

# Creating a tuple - uses parentheses ()
my_tuple = (a, b, c, d)  # Immutable: cannot be changed after creation
print(f"Original tuple: {my_tuple}")
print(f"Allows duplicates: {my_tuple.count(20)} occurrences of 20")
print(f"Ordered: First element = {my_tuple[0]}, Last element = {my_tuple[-1]}")

# Tuples are IMMUTABLE - cannot add, remove, or modify elements
# my_tuple[0] = 100  # ❌ This would raise TypeError: 'tuple' object does not support item assignment
# my_tuple.append(40)  # ❌ AttributeError: 'tuple' object has no attribute 'append'

# Can only create a new tuple by concatenation
new_tuple = my_tuple + (40, 50)  # Creates a NEW tuple, doesn't modify original
print(f"Concatenated tuple: {new_tuple}")
print(f"Original unchanged: {my_tuple}")

print("\n" + "=" * 60)
print("LIST - Mutable, Ordered, Allows Duplicates")
print("=" * 60)

# Creating a list - uses square brackets []
my_list = [a, b, c, d]  # Mutable: can be changed after creation
print(f"Original list: {my_list}")
print(f"Allows duplicates: {my_list.count(20)} occurrences of 20")
print(f"Ordered: First element = {my_list[0]}, Last element = {my_list[-1]}")

# Lists are MUTABLE - can add, remove, and modify elements
my_list[0] = 100  # ✅ Can modify elements
print(f"After modifying index 0: {my_list}")

my_list.append(40)  # ✅ Can append new elements
print(f"After append(40): {my_list}")

my_list.insert(1, 15)  # ✅ Can insert at specific position
print(f"After insert(1, 15): {my_list}")

my_list.remove(20)  # ✅ Can remove elements (removes first occurrence)
print(f"After remove(20): {my_list}")

my_list.pop()  # ✅ Can pop last element
print(f"After pop(): {my_list}")

print("\n" + "=" * 60)
print("SET - Mutable, Unordered, NO Duplicates")
print("=" * 60)

# Creating a set - uses curly braces {}
my_set = {a, b, c, d}  # Mutable but unordered, automatically removes duplicates
print(f"Original set: {my_set}")
print(f"NO duplicates: Only unique values stored (20 appears once)")
print(f"Unordered: No indexing available")

# Sets are UNORDERED - cannot access by index
# print(my_set[0])  # ❌ TypeError: 'set' object is not subscriptable

# Sets are MUTABLE - can add and remove elements
my_set.add(40)  # ✅ Can add new elements
print(f"After add(40): {my_set}")

my_set.add(20)  # ✅ Adding duplicate has no effect
print(f"After add(20) again: {my_set} (no change)")

my_set.remove(30)  # ✅ Can remove elements
print(f"After remove(30): {my_set}")

my_set.discard(100)  # ✅ Discard doesn't raise error if element not found
print(f"After discard(100): {my_set} (no error)")

# my_set.remove(100)  # ❌ Would raise KeyError if element not found

print("\n" + "=" * 60)
print("SUMMARY COMPARISON")
print("=" * 60)

comparison = """
┌─────────────┬──────────┬──────────┬────────────┬──────────────┐
│ Feature     │ Tuple    │ List     │ Set        │ Use Case     │
├─────────────┼──────────┼──────────┼────────────┼──────────────┤
│ Mutable     │ NO ❌    │ YES ✅   │ YES ✅     │              │
│ Ordered     │ YES ✅   │ YES ✅   │ NO ❌      │              │
│ Duplicates  │ YES ✅   │ YES ✅   │ NO ❌      │              │
│ Indexing    │ YES ✅   │ YES ✅   │ NO ❌      │              │
│ Syntax      │ ()       │ []       │ {}         │              │
├─────────────┼──────────┼──────────┼────────────┼──────────────┤
│ append()    │ NO ❌    │ YES ✅   │ NO ❌      │ Use add()    │
│ add()       │ NO ❌    │ NO ❌    │ YES ✅     │              │
│ remove()    │ NO ❌    │ YES ✅   │ YES ✅     │              │
│ insert()    │ NO ❌    │ YES ✅   │ NO ❌      │              │
│ pop()       │ NO ❌    │ YES ✅   │ YES ✅     │ Random in set│
└─────────────┴──────────┴──────────┴────────────┴──────────────┘

WHEN TO USE:
• Tuple:  Fixed data that shouldn't change (coordinates, RGB values, database records)
• List:   Dynamic data that needs ordering and modification (shopping cart, task list)
• Set:    Unique values, membership testing, mathematical operations (tags, unique IDs)
"""

print(comparison)

# Performance note
print("\nPERFORMANCE NOTES:")
print("• Tuples: Faster than lists (immutable = optimized)")
print("• Sets: Fastest for membership testing (O(1) vs O(n) for list)")
print("• Lists: Most flexible but slower for large datasets")
