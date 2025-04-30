#!/bin/bash
# Usage: ./push_to_github.sh <github_repo_url>
# Example: ./push_to_github.sh https://github.com/yourusername/mystic-village-release.git

if [ -z "$1" ]; then
  echo "Error: GitHub repository URL required."
  echo "Usage: $0 <github_repo_url>"
  exit 1
fi

REPO_URL=$1

# Initialize git repository if not already
if [ ! -d ".git" ]; then
  git init
  git branch -M main
fi

# Add remote if not exists
if ! git remote | grep -q origin; then
  git remote add origin "$REPO_URL"
fi

# Add all files, commit, and push
git add .
git commit -m "Initial release of Mystic Village"
git push -u origin main
