    #OOPs

# Yeh hamari blueprint (Class) hai
class BiryaniShop:
    # __init__ ka matlab hai jab bhi naye plate banegi, usme kya hoga
    def __init__(self, type_of_biryani, price):
        self.dish = type_of_biryani  # Property 1
        self.rate = price            # Property 2

    # Yeh aik action (Method) hai jo biryani serve karega
    def serve(self):
        return f"Aap ki garam garam {self.dish} tayar hai! Price: Rs.{self.rate}"

# --- Ab hum Asal Plates (Objects) banate hain ---
plate1 = BiryaniShop("Chicken Biryani", 300)
plate2 = BiryaniShop("Beef Biryani", 400)

# Ab isko run kar ke dekhte hain
print(plate1.serve())  # Output: Aap ki garam garam Chicken Biryani tayar hai! Price: Rs.300
print(plate2.serve())  # Output: Aap ki garam garam Beef Biryani tayar hai! Price: Rs.400

# FC Mobile Card

class Player:
    def __init__(self,name,ovr):
        self.naam=name
        self.Ovr=ovr
    
    def show_card(self):
        print(f"This Player is {self.naam} and its Ovr is {self.Ovr}")
    
player1=Player("Ronaldo",120)
player2=Player("Mbappe",119)
player3=Player("Bellingham",119)

player3.show_card()
