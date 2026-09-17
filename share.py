class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        try: 
            amount=float(input("Kitni amount deposit krni hai?"))

            if amount<0:
                raise ValueError("Deposit amount should be greater than 0.")
        except ValueError as e:
            print(f"Error ({e})")
        else:

          self.balance += amount
          print(f"{amount} deposit ho gaye! Naya balance: {self.balance}")


# -------------------------------------------------------------
# TESTING SECTION (Yeh sirf tab chalega jab aap 'one.py' direct chalayenge)
# -------------------------------------------------------------
if __name__ == "__main__":
    print("=== ONE.PY TESTING MODE ===")
    
    # Testing Account Creation
    acc1=Account("Subhan")
    acc1.deposit()
    