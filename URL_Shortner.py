import pyshorteners
import webbrowser

long_url = input("Enter the URL to shorten \n ")
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
print("The Shortened URL is \n" + short_url)
url = short_url
webbrowser.open_new_tab(url)


