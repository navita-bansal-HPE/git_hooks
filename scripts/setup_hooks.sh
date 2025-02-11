#!/bin/bash

# Define hooks directory relative to the script location
hooks_directory="../.github/hooks_directory"

# Verify the script is executed in a Git repository
if [ ! -d "../.git" ]; then
    echo "Error: This script must be run from the 'scripts' folder within the repository structure."
    exit 1
fi

# Verify hooks directory exists
if [ ! -d "$hooks_directory" ]; then
    echo "Error: Hooks directory not found at $hooks_directory"
    exit 1
fi

# Copy hooks to the .git/hooks directory
cp -r "$hooks_directory/." ../.git/hooks/

# Make hooks executable
chmod +x ../.git/hooks/*

# Update Git configuration
git config --local core.hooksPath ../.git/hooks
git config --local commit.template ../.git/hooks/.gitmessage

# Install required Python tools
echo "Installing required Python tools..."
pip install --quiet autoflake isort pylint pydocstyle black || {
    echo "Error: Failed to install one or more tools. Please ensure pip is installed and available."
    exit 1
}


echo "Git hooks and configurations have been successfully set up."
