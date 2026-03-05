#!/bin/bash
set -e

VERSION=$1
if [ -z "$VERSION" ]; then
  echo "Usage: ./release.sh <version>  (e.g. ./release.sh 0.1.9)"
  exit 1
fi

# Validate semver-ish format
if ! echo "$VERSION" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+$'; then
  echo "Error: version must be in X.Y.Z format"
  exit 1
fi

# Check working tree is clean
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "Error: uncommitted changes present. Commit or stash them first."
  exit 1
fi

echo "Releasing $VERSION..."

# Bump version in both files
sed -i '' "s/^version = .*/version = \"$VERSION\"/" pyproject.toml
sed -i '' "s/__version__ = .*/__version__ = \"$VERSION\"/" src/df_gallery/__init__.py

git add pyproject.toml src/df_gallery/__init__.py
git commit -m "release $VERSION"
git tag "v$VERSION"
git push origin master --tags

echo "Done. Monitor the release at: https://github.com/flicht/df-gallery/actions"