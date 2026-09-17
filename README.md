Here is the complete, polished `README.md` file layout, including the MIT license badge and link built right in.

Create a file named `README.md` in your project folder, paste this into it, and you're good to go:

```markdown
# GitHub Activity CLI

A simple, lightweight command-line tool written in Python that fetches and summarizes a user's recent public GitHub activity—categorizing pushes and repository creations cleanly without the clutter.

## Features

- Fetches public events directly from the GitHub API using native Python libraries (`urllib` and `json`).
- Accepts dynamic command-line arguments so you can check any public GitHub username.
- Aggregates push events to show total actions per repository.
- Summarizes repository and branch creation events.

## Prerequisites

You just need **Python 3** installed on your machine. No extra third-party packages or `pip install` commands required!

## Usage

Run the script from your terminal by passing a GitHub username as an argument:

```bash
python github_activity.py <username>

```

### Example

```bash
python github_activity.py praisemuochukwu789

```

## Built With

* **Python** (Standard Library only: `json`, `urllib`, `sys`)

## License

This project is licensed under the [MIT License](LICENSE).