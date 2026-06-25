import random
import string

def generate_secure_password():
    print("====================================")
    # Yahan 'k' ko small kar diya hai taaki niche se match kare
    key_size_input = input("Specify password length: ").strip()
    
    if not key_size_input.isnumeric():
        print("Alert: Length must be a positive integer.")
        return
        
    pass_length = int(key_size_input)
    
    if pass_length < 1:
        print("Alert: Length should be at least 1 character.")
        return
        
    print("\n--- Choose Character Set ---")
    print("[A] Alphabets Only")
    print("[B] Alphanumeric (Letters + Digits)")
    print("[C] High Security (Letters + Digits + Special Characters)")
    
    user_option = input("Select complexity (A, B, or C): ").upper().strip()
    
    char_pool = string.ascii_letters
    
    if user_option == "B":
        char_pool += string.digits
    elif user_option == "C":
        char_pool += string.digits + string.punctuation
    elif user_option == "A":
        pass  
    else:
        print("Invalid option chosen! Applying High Security by default.")
        char_pool += string.digits + string.punctuation
        
    final_password = "".join(random.choice(char_pool) for _ in range(pass_length))
        
    print("\nGenerated Key:")
    print(f"-> {final_password}")
    print("====================================")

if __name__ == "__main__":
    generate_secure_password()