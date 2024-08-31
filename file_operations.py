
def read_from_file(file_path):   
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        print(f"Data read from {file_path} successfully.")
        return data
    except Exception as e:
        print(f"An error occurred while reading from the file: {e}")
        return None


def write_to_file(file_path, data):
    
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        print(f"Data written to {file_path} successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def append_to_file(file_path, data):
    
    try:
        with open(file_path, 'a') as file:
            file.write(data)
        print(f"Data appended to {file_path} successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")


