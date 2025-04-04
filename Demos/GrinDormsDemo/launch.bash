#!/bin/bash

# Create logs directory if it doesn't exist
mkdir -p ~/logs

# Get current commit hash and timestamp
commit_hash=$(git rev-parse HEAD)
timestamp=$(date +"%Y-%m-%d %T")

# Create log file with commit in filename
log_file="$HOME/logs/log_cmt:$commit_hash:$(date +%Y-%m-%d).txt"

script "$log_file"

# Write commit and timestamp to log file
echo "Commit: $commit_hash"
echo "Timestamp: $timestamp"

# Install required packages
pip install django django-environ pillow python-dotenv psycopg2

# Define manage.py path (using POSIX path format)
manage_path="ROOT/Demos/GrinDormsDemo/manage.py"
settings_path="ROOT/Demos/GrinDormsDemo/grindormsdemo/settings.py"

echo -e "\nChecking settings to ensure security..."
if grep -q "DEBUG = True" "$settings_path"; then
    echo "\nDeployment Failed, incorrect process for deployment executed, use Github actions. Symlink switch may have failed." >&2
else
    # Run Django commands and log output
    echo -e "\nRunning migrations..."
    python "$manage_path" migrate

    echo -e "\nStarting server..."
    python "$manage_path" runserver csc-234.us.reclaim.cloud:8080 --noreload &
fi