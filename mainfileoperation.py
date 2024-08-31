from file_operations import write_to_file, append_to_file, read_from_file

def main_menu():
    while True:
       
        print("1. Write to a file")
        print("2. Append to a file")
        print("3. Read from a file")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            file_path = input("Enter the file path: ")
            data = input("Enter the data to write: ")
            write_to_file(file_path, data)        

        elif choice == '2':
            file_path = input("Enter the file path: ")
            data = input("Enter the data to append: ")
            append_to_file(file_path, data)

        elif choice == '3':
            file_path = input("Enter the file path: ")
            content = read_from_file(file_path)
            if content is not None:
                print("File Content:\n", content)
        
        elif choice == '4':
            print(" Goodbye!")
            break
        
        else:
            print("Invalid choice")


main_menu()

