url = input("URL: ").strip()

# str.replace
username = url.replace("https://twitter.com","")

print(f"Username: {username}")