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
re.search(r"^https?://(www\.)?twitter\.com/(.+)$", urll, re.IGNORECASE)
if matches:
# the subdomain is optional and to make it optional there needs to be parenthesis. now that theres a second set of parenthesis group 1 must be changed to group 2
print(f"Username:", matches.group(1))
