def display_inventory(file_path):
    try:
        with open(file_path, 'r') as file:
            print("Inventory Contents:\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")


file_path = "D:\PW live Assignment\inventory.txt"
display_inventory(file_path)
