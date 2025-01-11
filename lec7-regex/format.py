name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(",")
    name = f"{first}{last}"
print(f"hello, {name}")
# even with this fix, something like a comma or no space to split comma could break this code

# the version of split thats built in the str variable does not accept regex
# re library must be imported
import re

name = input("What's your name? ").strip()
re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first}{last}"
print(f"hello, {name}")
