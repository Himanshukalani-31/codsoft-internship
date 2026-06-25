class PhoneDirectory:
    def __init__(self):
        # Global list ki jagah class dictionary use ki hai storage ke liye
        self.records = {}

    def create_record(self):
        print("\n📥 --- Register New Entry ---")
        full_name = input("Enter Full Name: ").strip()
        phone_num = input("Enter Phone Number: ").strip()
        email_id = input("Enter Email Address: ").strip()
        location = input("Enter Physical Address: ").strip()
        
        # Validation rules ka style change kiya
        if not full_name or not phone_num:
            print("Operation Failed: Name and Phone are mandatory fields.")
            return
            
        # Phone number ko uniquely main key bana diya
        self.records[phone_num] = {
            "name": full_name,
            "email": email_id,
            "address": location
        }
        print(f"Success: Saved contact details for '{full_name}'.")

    def display_all(self):
        print("\n📖 --- Saved Directory ---")
        if not self.records:
            print("The directory is currently empty.")
            return
            
        # Index tracking ka naya tarika
        for serial, (phone, details) in enumerate(self.records.items(), start=1):
            print(f"[{serial}] {details['name']} -> Mob: {phone}")

    def locate_record(self):
        print("\n🔍 --- Search Database ---")
        search_term = input("Search by keyword (name/number): ").strip().lower()
        
        match_found = False
        for phone, info in self.records.items():
            if search_term in info['name'].lower() or search_term in phone:
                print(f"\n[Match Found]")
                print(f" Name    : {info['name']}")
                print(f" Phone   : {phone}")
                print(f" Email   : {info['email'] if info['email'] else 'N/A'}")
                print(f" Address : {info['address'] if info['address'] else 'N/A'}")
                match_found = True
                
        if not match_found:
            print("No matching records found in the directory.")

    def modify_record(self):
        print("\n✏️ --- Modify Existing Entry ---")
        target_phone = input("Enter the EXACT Phone Number of the contact: ").strip()
        
        if target_phone in self.records:
            print("Press 'Enter' to skip editing any specific field.")
            current_info = self.records[target_phone]
            
            upd_name = input(f"New Name [{current_info['name']}]: ").strip()
            upd_email = input(f"New Email [{current_info['email']}]: ").strip()
            upd_addr = input(f"New Address [{current_info['address']}]: ").strip()
            
            if upd_name:
                current_info['name'] = upd_name
            if upd_email:
                current_info['email'] = upd_email
            if upd_addr:
                current_info['address'] = upd_addr
                
            print("Success: Record updated successfully.")
        else:
            print("Error: No record exists with this phone number.")

    def erase_record(self):
        print("\n❌ --- Remove Entry ---")
        target_phone = input("Enter the EXACT Phone Number to delete: ").strip()
        
        if target_phone in self.records:
            removed_person = self.records[target_phone]['name']
            # Direct deletion without loop
            del self.records[target_phone]
            print(f"Success: '{removed_person}' has been removed from database.")
        else:
            print("Error: Provided phone number not found.")


def launch_directory():
    book = PhoneDirectory()
    
    while True:
        print("\n==============================")
        print("      CONTACT MASTER PRO      ")
        print("==============================")
        print(" [A] Add New Contact")
        print(" [B] View All Contacts")
        print(" [C] Find a Contact")
        print(" [D] Edit Contact Details")
        print(" [E] Delete a Contact")
        print(" [Q] Quit Application")
        
        user_pick = input("\nSelect Option (A-Q): ").strip().upper()
        
        if user_pick == 'A':
            book.create_record()
        elif user_pick == 'B':
            book.display_all()
        elif user_pick == 'C':
            book.locate_record()
        elif user_pick == 'D':
            book.modify_record()
        elif user_pick == 'E':
            book.erase_record()
        elif user_pick == 'Q':
            print("\nShutting down directory. Goodbye!")
            break
        else:
            print("Invalid input! Please select a valid code from the menu.")

if __name__ == "__main__":
    launch_directory()