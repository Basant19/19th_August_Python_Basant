def calculate_total_expenses(file_path):
   
    total_expenses = 0.0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    
                    expense = float(line.strip())
                    total_expenses += expense
                except ValueError:
                    print(f"Invalid line detected (not a number): {line.strip()}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    
    return total_expenses


file_path = "D:\PW live Assignment\expenses.txt"
total = calculate_total_expenses(file_path)
    
if total is not None:
        print(f"Total Expenses: {total:.2f}")
