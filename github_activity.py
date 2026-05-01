import sys 
import urllib.request
import json


def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            return json.loads(data)

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("User not found.")
        else:
            print(f"HTTP Error: {e.code}")
    
    except urllib.error.URLError:
        print("Failed to connect. Check your internet.")

    except Exception as e:
        print(f"Unexpected error: {e}")
    
    return None 

def main():
    if len(sys.argv) < 2:
        print("Usage: python github_activity.py <username>")
        return 
    
    username = sys.argv[1]
    print(f"Fetching activity for user: {username}")

    events = fetch_github_activity(username)

    if events is None:
        return    

if __name__ == "__main__":
    main()
