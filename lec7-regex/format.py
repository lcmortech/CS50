name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(",")
    name = f"{first}{last}"
print(f"hello, {name}")
# even with this fix, something like a comma or no space to split comma could break this code