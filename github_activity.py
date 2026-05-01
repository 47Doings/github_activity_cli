import sys
import urllib.request
import urllib.error
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


def display_activity(events):
    if not events:
        print("No recent activity found.")
        return

    count = 0

    for event in events:
        if count >= 10:  # limit output
            break

        event_type = event.get("type")
        repo = event.get("repo", {}).get("name")

        if event_type == "PushEvent":
            commits = event.get("payload", {}).get("commits", [])
            if len(commits) > 0:
                print(f"- Pushed {len(commits)} commits to {repo}")
                count += 1

        elif event_type == "IssuesEvent":
            print(f"- Opened an issue in {repo}")
            count += 1

        elif event_type == "WatchEvent":
            print(f"- Starred {repo}")
            count += 1

        elif event_type == "CreateEvent":
            print(f"- Created repository or branch in {repo}")
            count += 1

        # ignore noisy/empty events


def main():
    if len(sys.argv) < 2:
        print("Usage: python github_activity.py <username>")
        return

    username = sys.argv[1]
    print(f"Fetching activity for user: {username}")

    events = fetch_github_activity(username)

    if events is None:
        return

    display_activity(events)


if __name__ == "__main__":
    main()