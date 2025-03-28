#!/bin/bash

# Create logs directory if it doesn't exist
mkdir -p ~/logs

# Get current commit hash and timestamp
commit_hash=$(git rev-parse HEAD)
timestamp=$(date +"%Y-%m-%d %T")

# Create log file with commit in filename
log_file="$HOME/logs/log_cmt:$commit_hash:$(date +%Y-%m-%d).txt"

# Write commit and timestamp to log file
echo "Commit: $commit_hash" | tee -a "$log_file"
echo "Timestamp: $timestamp" | tee -a "$log_file"

# Install required packages
pip install django django-environ | tee -a "$log_file"

# Define manage.py path (using POSIX path format)
manage_path="./Demos/GrinDormsDemo/manage.py"

# Run Django commands and log output
{
    echo -e "\nRunning migrations..."
    python "$manage_path" migrate
    
    echo -e "\nStarting server..."
    python "$manage_path" runserver
} | tee -a "$log_file"