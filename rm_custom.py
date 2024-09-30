#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    # Get the arguments passed to the script
    args = sys.argv[1:]

    if len(args) < 1:
        print("Usage: rm.py [-r] target...")
        sys.exit(1)

    # Separate the flags (e.g., -r) from the targets
    targets = [arg for arg in args if not arg.startswith('-')]
    options = [arg for arg in args if arg.startswith('-')]

    # Check if there are multiple targets and ensure each one exists
    if len(targets) == 0:
        print("Error: No files or directories specified for removal.")
        sys.exit(1)

    # Check if any of the targets are directories
    has_directory = any(os.path.isdir(target) for target in targets)

    # If a directory is being deleted and -r is not provided, ask the user
    if has_directory and '-r' not in options and '-R' not in options:
        response = input("One or more targets are directories. Would you like to add the -r option to remove them recursively? (y/n): ").strip().lower()
        if response == 'y':
            options.append('-r') # Add the -r option
        else:
            print("Operation aborted.")
            sys.exit(1)

    # Call the original rm command with the options and targets
    try:
        subprocess.run(['rm'] + options + targets, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
