print()
print("Replit Login System")
print()
def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password?: ")
    print()
    if username == "david" and password == "baldies4life":
      print("Welcome to Replit!")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      print()
      continue

login()