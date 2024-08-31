def add_employee_to_file(file_path):
   
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    salary = input("Enter employee salary: ")

    with open(file_path, 'a') as file:
        file.write(f"Name: {name}, Age: {age}, Salary: {salary}\n")
    
    print(f"Employee {name}'s details added to {file_path} successfully.")

def show_employees(file_path):
  
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if content:
                print("\nEmployee Details:\n")
                print(content)
            else:
                print("\nNo employee data found.\n")
    except FileNotFoundError:
        print(f"\nFile {file_path} not found. Please add employees first.\n")

def main_menu():
    file_path = "employees.txt"
    
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Show Employees")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_employee_to_file(file_path)
        
        elif choice == '2':
            show_employees(file_path)

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


main_menu()
