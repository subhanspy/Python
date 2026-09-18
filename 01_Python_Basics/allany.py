#all and any (all for validation all are true?? .... any for is there any fault????)
customer = ["Subhan", "subhan@gmail.com", "03001234567"]


is_record_complete = all(bool(field) for field in customer)

print("Is customer record complete?:", is_record_complete)
