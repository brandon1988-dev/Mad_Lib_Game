""" Mad Libs Generator
----------------------------------------
"""
# Loop back to this point once code finishes
loop: int = 1
while loop < 10:
    p_noun = input("Choose a plural noun: ")
    adjective = input("Choose an adjective: ")
    noun = input("Choose a noun: ")
    animal = input("Name an animal: ")
    verb = input("Choose a verb (Base Form): ")
    noun2 = input("Choose a noun: ")
    verb2 = input("Choose a verb (Base Form): ")
    verb3 = input("Choose a verb (Base Form): ")
    noun3 = input("Choose a noun: ")
    noun4 = input("Choose a noun: ")

# Displays the story based on the users input
    print("------------------------------------------")
    print("When Amazon launched in 1995 as a website that only sold " + p_noun + "founder Jeff Bezos had a vision for"
          " the company's " + adjective + " growth and commerce domination.")

    print("------------------------------------------")
# Loop back to "loop = 1
    loop = loop + 1


