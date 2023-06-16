import os

def replace_prefix_in_file(files, prefix, new_prefix):
    #For each file, read the file in binary mode and replace all instances of the prefix with the new prefix
    for file_path in files:
        with open(file_path, 'rb') as file:  # Open the file in binary mode
            content = file.read() #read the file and encode in utf-8
        if prefix.encode('utf-8') in content:
            updated_content = content.replace(prefix.encode('utf-8'), new_prefix.encode('utf-8')) #replace all instances of old instance scope

            with open(file_path, 'wb') as file:  # Open the file in binary mode
                file.write(updated_content) # update file with new contents
                print(f"File cleanup run for {file_path}") # Print impacted files to the terminal

def rename_dirs_and_files(paths, prefix, new_prefix):
    for path in paths:
        if prefix in path:
            # Only replace last instance of prefix so files get renamed, then dirs on their own loop
            path_list = path.rsplit(prefix, 1)
            new_path  = new_prefix.join(path_list)
            os.rename(path, new_path) # Update the name of the file or directory
            print(f"Renamed {path} to {new_path}") # Print impacted file or dir with new path to terminal

# Specify the root directory and the prefix you want to match
file_prefix    = 'x-71146' # Prefix from our original working file
new_prefix     = input("Enter your instance prefix: ")  # User Input to get new instance scope Use raw_input() in Python 2

# Call functions to replace scope prefixes in file contents & to rename directories, & files
# First cleanup file contents, then files, then directories to ensure the no "file not found" errors

#Files to scrub & replace prefix
files      = ['REST-API-Explorer-Example/now-ui.json',
              'REST-API-Explorer-Example/src/index.js',
              'REST-API-Explorer-Example/src/x-71146-testing-project/index.js',
              'REST-API-Explorer-Example/src/x-71146-testing-project/__tests__/test.x-71146-testing-project.js',
              'REST-API-Explorer-Example/README.md']
replace_prefix_in_file(files, file_prefix, new_prefix)

##Directories and files to rename
dirs_and_files = ['REST-API-Explorer-Example/src/x-71146-testing-project/__tests__/test.x-71146-testing-project.js',
                  'REST-API-Explorer-Example/src/x-71146-testing-project']
rename_dirs_and_files(dirs_and_files, file_prefix, new_prefix)
