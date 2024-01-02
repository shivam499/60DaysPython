import webbrowser

user_term = input("Enter the search: ").replace(' ', '+')

webbrowser.open(f"https://www.google.com/search?q={user_term}")
