from pakudex import Pakudex


pakudex = Pakudex(capacity=5)
# species = "psygoose"
# pakudex.add_pakuri(species)

def menu():
    return ("\nPakudex Main Menu\n-----------------\n1. List Pakuri"
          "\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit\n")


if __name__ == "__main__":

    print("Welcome to Pakudex: Tracker Extraordinaire!")

# try and except to catch invalid sizes
    while True:
        try:
            size = int(input("Enter max capacity of the Pakudex: "))
            if size <= 0:
                print("Please enter a valid size. ")
            else:
                break
        except:
            print("Please enter a valid size. ")

    print(f"The Pakudex can hold {size} species of Pakuri.")
# create object to call functions
    paku = Pakudex(size)

    while True:

        print(menu())
        menu_option = input("What would you like to do? ")


        if menu_option == '1':
            if paku.get_species_array() == None: # error messge if none
                print("\nNo Pakuri in Pakudex yet!")
            else:
                print("\nPakuri In Pakudex:")
                # iterate through list to print out pakuri
                for i in range(0, len(paku.get_species_array())):
                    print(f"{i + 1}. {paku.get_species_array()[i]}\n")


        elif menu_option == '2':
            sp = input("\nEnter the name of the species to display: ")
            stats = paku.get_stats(sp)
            # index stats
            if stats:
                print(f"Species: {sp}")
                print(f"Attack: {(stats[0])}")
                print(f"Defense: {(stats[1])}")
                print(f"Speed: {(stats[2])}\n")
            else:
                print("Error: No such Pakuri!\n")



        elif menu_option == '3':
            if paku.size >= paku.capacity:
                print("Error: Pakudex is full!")
            # check capacity error before prompting for input
            else:
                species = input("\nEnter the name of the species to add: ")
                # check for true and false in add_pakuri method
                if paku.add_pakuri(species) == False:
                    print("Error: Pakudex already contains this species!\n")
                else:
                    paku.add_pakuri(species)
                    print(f"Pakuri species {species} successfully added!")


        elif menu_option == '4':
            sp = input("Enter the name of the species to evolve: ")
            # check true and use function if true
            if paku.evolve_species(sp):
                print(f"{sp} has evolved!\n")
            else:
                print("Error: No such Pakuri!\n")

        elif menu_option == '5':
            # call sort
            paku.sort_pakuri()
            print("Pakuri have been sorted!\n")

        elif menu_option == '6':
            print("\nThanks for using Pakudex! Bye!\n")
            break # end program

        else:
            print("\nUnrecognized menu selection!") # all other values



