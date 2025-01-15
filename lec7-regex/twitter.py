url = input("URL: ").strip()

# str.replace
# removes all the url
# username = url.replace("https://twitter.com","")
# removes only the part of the string needed
username = url.removeprefix("https://twitter.com")
print(f"Username: {username}")