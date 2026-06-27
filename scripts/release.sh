#!/bin/bash

echo "Running Python syntax check..."
python3 -m py_compile tools/*.py

echo "Checking Git status..."
git status

echo "Creating release tag..."
git tag -a v1.0.0 -m "Initial Release"

echo "Pushing tag..."
git push origin v1.0.0

echo "Release completed."
