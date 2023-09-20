from computer import *
from oo_resale_shop import *


def main():
    # Create shop instance
    shop = ResaleShop() 
    computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Create computer and add to the resale store's inventory
    print(shop.buy(computer))
    computer_ID = shop.inventory.index(computer)
    print("Buying", computer.description)
    print("Adding to inventory...")
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.store_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_ID, ", updating OS to", new_OS)
    print("Updating inventory...")
    shop.refurbish(computer, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.store_inventory()
    print("Done.\n")

    # Now, let's sell it!
    print("Selling Item ID:", computer_ID)
    shop.sell(computer_ID)

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.store_inventory()
    print("Done.\n")

main()
