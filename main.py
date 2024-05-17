import os
import subprocess

def insert_toc_in_md_files(directory):
    # Loop through all files in the given directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file is a markdown file
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                # Execute the command to insert the TOC
                command = f'~/gh-md-toc --no-backup {filepath}'
                # print(f"Running command: {command}")
                try:
                    print(f"Running command: {command}")
                    subprocess.run(command, shell=True, check=True)
                    print(f"Successfully inserted TOC in {filepath}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to insert TOC in {filepath}: {e}")

if __name__ == "__main__":
    # Replace 'your_directory' with the path to your target directory
    directory = './'
    insert_toc_in_md_files(directory)
