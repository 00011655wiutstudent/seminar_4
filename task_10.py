'''Write a program that will ask to input the module name and number of
components on the module with corresponding weighting. It should also ask to
enter mark for the components and show you the final mark.
Additionally you may include a feature, where user can input the desired overall
mark for the module and program outputs the required marks for the components.
Save it to in seminar4/ folder
Push your updates to Github repository.'''

input("What is the name of the module ?:")
components = input("how many components in this module ?")
print("You are preparing for " + components)
first = input("what is your mark for first component ?")
second = input("What is your mark for second component ?")
first_mark = int(first)
second_mark = int(second)
mark = first_mark * 0.4 + second_mark * 0.6
print(f"Your total mark is: {mark}")
