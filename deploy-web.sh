#!/bin/bash
# Manual fallback for the CI deploy (.github/workflows/deploy.yml).
set -e

echo -e "\033[0;32mDeploying updated website to cbjuan.github.io...\033[0m"

# Build the project and its search index, same as CI.
pnpm install --frozen-lockfile
hugo --gc --minify
pnpm run pagefind

# Go To Public folder
cd public
# Add changes to git.
git add .

# Commit changes.
msg="Updating website -> `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin master

# Come Back up to the Project Root
cd ..