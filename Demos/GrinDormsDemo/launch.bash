#!/bin/bash

# Create logs directory if it doesn't exist
mkdir -p ~/logs

# Get current commit hash and timestamp
commit_hash=$(git rev-parse HEAD)
timestamp=$(date +"%Y-%m-%d %T")

# Create log file with commit in filename
log_file="$HOME/logs/log_cmt:$commit_hash:$(date +%Y-%m-%d).txt"

script "$logfile"

# Write commit and timestamp to log file
echo "Commit: $commit_hash"
echo "Timestamp: $timestamp"

# Install required packages
pip install django django-environ pillow

# Define manage.py path (using POSIX path format)
manage_path="./Demos/GrinDormsDemo/manage.py"
settings_path="./Demos/GrinDormsDemo/grindormsdemo/settings.py"

echo -e "\nChecking settings to ensure security..."
if [grep "DEBUG = True"] then
    >&2 echo "\nDeployment Failed, incorrect process for deployment executed, use Github actions. Symlink switch may have failed."
    exit
else
    # Run Django commands and log output
    echo -e "\nRunning migrations..."
    python "$manage_path" migrate

    echo -e "\nStarting server..."
    python "$manage_path" runserver
    exit
exit