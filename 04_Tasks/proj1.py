class ContactBook():
    def __init__ (self):
        self.contacts=[]
    
    def get_valid_phone(self):

        while True:
            try:
               
               Num_1=int(input("Please enter the Number."))

            except ValueError:
                print("Please enter the number only!!")
                continue
            
            
            else:
             print(f"Number found {Num_1}")
            return Num_1


    def add_contact(self):
        Name=input("Enter name:")
        Number=self.get_valid_phone()
        
        contact={"Name":Name,"Number":Number}
        self.contacts.append(contact)
        print(f"Contact {Name} saved successfully")
        
    def view_contacts(self):

        if not self.contacts:
            print("Contacts not found!!")
        for c in self.contacts:
                print(f"Name: {c['Name']} | Number: {c['Number']}")
            
        else:
            print("Your Contacts:")


if __name__ == "__main__":
    book = ContactBook()

    while True:
        print("===MENU===")
        print("1.Add Contact")
        print("2.View Contact")
        print("3.Exit")

        choice = input("Choose option (1 to 3):")

        if choice == "1":
            book.add_contact()
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            print("Exit")
            break
        else:
            print("Plese select the given options only.")
