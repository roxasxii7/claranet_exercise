import os

def read_first_line_in_directory(directory_path):
    try:
        # Check if the provided path is a valid directory
        if not directory_path:
            return "The provided directory path is empty."
        
        if not os.path.exists(directory_path):
            return "The provided directory path does not exist."

        if not os.path.isdir(directory_path):
            return "The provided path is not a directory."

        # Initialize an empty dictionary to store results (filename: first_line)
        counter = {}

        # List all files in the directory
        file_list = os.listdir(directory_path)

        # Iterate through the files
        for filename in file_list:
            file_path = os.path.join(directory_path, filename)
            # Check if the current item is a file
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    first_line = file.readline().strip()
                    script = first_line.startswith('#!')
                    if not (first_line in counter):
                        if(script):
                            counter[first_line] = 1
                    else:
                        c = counter[first_line]
                        update = {first_line : c+1}
                        counter.update(update)

        return counter

    except Exception as e:
        return f"An error occurred: {str(e)}"

directory_path = input("Insert the directory: ")
result = read_first_line_in_directory(directory_path)

if isinstance(result, dict):
    if not result:
        print("No script lines found in the provided directory.")
    else:
        for script, occurrences in result.items():
            print(f"{occurrences} {script}")
else:
    print(result)