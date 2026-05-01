# GitHub Activity CLI

A simple command-line tool that fetches and displays the recent public activity of any GitHub user using the GitHub API.

---

##  Features

* Fetches recent GitHub user activity
* Displays clean, readable terminal output
* Handles errors (invalid users, network issues)
* Built using only Python standard libraries (no external packages)

---

##  Tech Stack

* Python 3
* urllib (for HTTP requests)
* JSON (for parsing API responses)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/github_activity_cli.git
cd github_activity_cli
```

Make sure you have Python 3 installed.

---

## ▶️ Usage

Run the script from the terminal:

```bash
python github_activity.py <username>
```

### Example:

```bash
python github_activity.py torvalds
```

---

## Sample Output

```text
Fetching activity for user: torvalds
- Pushed 3 commits to linux/linux
- Opened an issue in repo-name
- Starred repo-name
```

---

## ⚠️ Limitations

* Only shows **recent public activity** (not full history)
* Some events may not include full commit details
* GitHub API rate limits unauthenticated requests

---

## 🎯 What I Learned

This project helped me practice:

* Working with APIs in Python
* Handling JSON data
* Building CLI applications
* Error handling and defensive programming

---

## 🔮 Future Improvements

* Add colored terminal output
* Filter event types
* Convert into installable CLI tool (`github-activity <user>`)
* Add caching to reduce API calls

---

## 📌 Author

Built as a learning project to practice Python and API integration.
