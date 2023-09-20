from computer import *

class ResaleShop():

    # What attributes will it need?
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # What methods will you need?
    def store_inventory(self):    
        if self.inventory:
            for computer in self.inventory:
                print(f'''
                Item ID: {self.inventory.index(computer)}{computer}''')
        else:
            print("No inventory to display.")
       
    def refurbish(self, computer, new_os):
        if computer in self.inventory:
            if computer.year_made < 2000:
                computer.price = 0 # too old to sell, donation only
            elif computer.year_made < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif computer.year_made < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print(f"Item", {computer}, "not found. Please select another item to refurbish.")

    def create_computer(self,description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
         computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
         return computer
    
    def buy(self,computer):
        self.inventory.append(computer)

    def sell(self, id):
        computer = self.inventory[id]
        if  computer in self.inventory:
            self.inventory.remove(computer)
            print(f"Item {id} sold!")
        else: 
            print(f"Item {id} not found. Please select another item to sell.") 

'''
    - storing information about a specific computer
    - storing the inventory for the store
    - updating a computer's price
    - updating a computer's OS
    - buying a computer (add to inventory)
    - selling a computer (remove from inventory)
    - refurbishing a computer 
'''

        # 1. call Computer(...) constructor
        #   to create a new Computer instance

        # 2. call inventory.append(...) to add
        #   the new Computer instance to the inventory

def main():
    my_store = ResaleShop()
    computer = my_store.create_computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    
    my_store.buy(computer)
    my_store.store_inventory()
    
    my_store.sell(0)
    my_store.store_inventory()
 
    
main()