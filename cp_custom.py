#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    # Get the arguments passed to the script
    args = sys.argv[1:]

    if len(args) < 2:
        print("Usage: cp.py [-r] source... destination")
        sys.exit(1)

    # Destination is always the last argument
    destination = args[-1]

    # Check if multiple sources are provided
    sources = args[:-1]

    # Check if the destination exists and is a directory when copying multiple sources
    if len(sources) > 1 and not os.path.isdir(destination):
        print(f"Error: When copying multiple files or directories, the destination '{destination}' must be a directory.")
        sys.exit(1)

    # Check if any of the sources are directories
    has_directory = any(os.path.isdir(source) for source in sources)

    # If a directory is being copied, ensure -r is used
    if has_directory:
        if '-r' not in args and '-R' not in args:
            # Prompt the user to confirm adding the -r flag
            response = input(f"One or more sources are directories. Would you like to add the -r option? (y/n): ").strip().lower()
            if response == 'y':
                sources.insert(0, '-r') # Add the -r option before the sources
            else:
                print("Operation aborted.")
                sys.exit(1)

    # Call the original cp command with the arguments (includes source and destination)
    try:
        subprocess.run(['cp'] + sources + [destination], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

