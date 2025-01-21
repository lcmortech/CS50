#url = input("URL: ").strip()

# str.replace
# removes all the url
# username = url.replace("https://twitter.com","")
# removes only the part of the string needed
#username = url.removeprefix("https://twitter.com")
#print(f"Username: {username}")

# re.sub(pattern, replaced string, newer string, count=0, flags=0)

# find and replace using regex
import re

url = input("URL: ").strip()

# username = re.sub(r"^https?://(www\.)?twitter\.com/", "", url)
# username = url.removeprefix("https://twitter.com/")
# make the whole https part optional
# username = re.sub(r"^(https?:)?://)?(www\.)?twitter\.com/","", url)
# alt (looks a little less obvious): username = re.sub(r"^(https?:)?://)?(www\.|)twitter\.com/","", url)
re.search(r"^https?://(www\.)?twitter\(?:com|org)/(.+)$", url, re.IGNORECASE)
#if matches:
# the subdomain is optional and to make it optional there needs to be parenthesis. now that theres a second set of parenthesis group 1 must be changed to group 2

if matches.group(1) == "com":
    print(f"Username:", matches.group(1))

 # you can add the walrus operator to tighten things up
 #A|B - either A or B
#(...) - a group
# (?:...) - non capturing version - similar to a ternary operator (it does not need to be captured)
# like (?:com|org) - because either is fine
# or
# if matches.group(1) == "com":
    # print(f"Username:", matches.group(1))
# to capture "com" outside of using regex
# ([a-z0-9_]+) is more precise and supported by twitter
# there is also re.split() and re.findall()
# re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, string, flags=0)