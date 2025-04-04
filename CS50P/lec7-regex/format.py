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
re.search(r"^(.+), *(.+)$", name)
if matches:
    last = matches.groups(1)
    first = matches.groups(2)
    name = f"{first}{last}"
# alt: name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

# re.search
# looking for a name with no space will still break it (can be solved by adding an asterisk)