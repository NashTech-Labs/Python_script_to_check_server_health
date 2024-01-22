import requests

# Create a session object to persist certain parameters across requests
session = requests.Session()

def check_server(url):
    try:
        # Use the session object to send the GET request
        response = session.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# List of URLs to check
urls = ["http://example.com", "http://otherexample.com"]

# Check each server and print whether it's up or down
for url in urls:
    if check_server(url):
        print(f"{url} is up and running fine")
    else:
        print(f"{url} is down, you have got some extra work to do!")
