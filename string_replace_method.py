# """
# I love Pizza!
# Pizza is my guilty pleasure.
# Pizza should be declared King of Foods.
# """
# not a fan anymore - how to modify this message using string method replace

base_str = """
I love Pizza!
Pizza is my guilty pleasure.
I think Pizza should be served at every meal.
Pizza should be declared King of Foods.
"""
print(base_str)

result = base_str.replace("Pizza", "Ice cream")

print(result)

print("****************")

print(base_str.replace("Pizza", "ice cream"))

print("++++++++++++++++")

result = base_str.replace("Pizza", "ice cream", 3)

print(result)