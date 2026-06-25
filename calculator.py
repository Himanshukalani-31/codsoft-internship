def execute_calculation():
    print("====== DIGITAL CALCULATOR ======\n")
    
    # Input lene ka aur validation ka tarika badal diya
    first_input = input("Enter the First Number: ")
    try:
        val1 = float(first_input)
    except ValueError:
        print("Error: That is not a valid numerical input.")
        return
        
    print("\nAvailable Operators:")
    print(" -> [A] Addition")
    print(" -> [S] Subtraction")
    print(" -> [M] Multiplication")
    print(" -> [D] Division")
    
    op_action = input("\nSelect your operator (A/S/M/D or +, -, *, /): ").upper().strip()
    
    second_input = input("Enter the Second Number: ")
    try:
        val2 = float(second_input)
    except ValueError:
        print("Error: That is not a valid numerical input.")
        return

    print("\n--------------------------------")
    # Match-case ya alag structure use karke logic badla
    if op_action in ['A', '+']:
        output = val1 + val2
        print(f"Sum Result: {val1} + {val2} = {output}")
        
    elif op_action in ['S', '-']:
        output = val1 - val2
        print(f"Difference Result: {val1} - {val2} = {output}")
        
    elif op_action in ['M', '*']:
        output = val1 * val2
        print(f"Product Result: {val1} * {val2} = {output}")
        
    elif op_action in ['D', '/']:
        if val2 == 0.0:
            print("Math Error: Division by zero is undefined.")
        else:
            output = val1 / val2
            print(f"Quotient Result: {val1} / {val2} = {output}")
            
    else:
        print("Error: Unrecognized operation selected.")
    print("--------------------------------")

if __name__ == "__main__":
    execute_calculation()