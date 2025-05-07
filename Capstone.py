"""
Capstone
# List containing full names of students
names = ["Liam Johnson", "Ava Martinez", "Noah Smith", "Emma Davis", "Jackson Garcia"]
# Corresponding list of their birthdays in MM/DD/YYYY format
bds = ["03/15/2007", "11/02/2006", "08/25/2008", "07/10/2007", "04/29/2006"]
# Favorite colors associated with each student
fav_col = ["blue", "pink", "green", "red", "yellow"]

# Greeting message for the user
print("Welcome to the Birthday Organizer!\n")

while True:
    # Display a simple menu for user interaction
    print("\nMenu:")
    print("1. View students (with censored birthdays)")
    print("2. Reveal a student's full name and birthday")
    print("3. Add a new student")
    print("4. Quit")

    # Prompt the user to make a selection from the menu
    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        # Display the list of students, but censor their birthdays for privacy
        print("\nHere are the available students:")
        for name in names:
            # Extract and display only the first name
            first_name = name.split()[0]  
            print("- " + first_name + ": Birthday (CENSORED)")
    
    elif choice == "2":
        # Allow the user to reveal a specific student's birthday by guessing their favorite color
        student_name = input("\nEnter the first name of the student whose birthday you want to see: ").strip()
        # index variable to track the student's position
        index = None
        for i in range(len(names)):
            # Check if first name matches user input
            if names[i].split()[0].lower() == student_name.lower():  
                index = i
                break

        if index is not None:
            # The user must correctly guess the student's favorite color before revealing their birthday
            while True:
                color_guess = input("What is " + student_name + "'s favorite color? ").strip().lower()
                # Check if the guessed color matches the stored favorite color
                if color_guess == fav_col[index]:  
                    # Retrieve the student's full name
                    full_name = names[index]  
                    print("Correct! " + full_name + "'s birthday is " + bds[index] + ".")
                    # Exit the loop once the correct color is guessed
                    break  
                else:
                    print("Incorrect color! Try again.")
        else:
            print("That student is not in the list. Please check the name and try again.")

    elif choice == "3":
        # Allow the user to add a new student with their birthday and favorite color
        new_name = input("Enter the full name of the new student: ").strip()
        new_bd = input("Enter their birthday (MM/DD/YYYY): ").strip()
        new_color = input("Enter their favorite color: ").strip().lower()
        # Add the new name to the list
        names.append(new_name)
        # Add the corresponding birthday
        bds.append(new_bd)  
        # Store the student's favorite color
        fav_col.append(new_color) 
        
        print("New student added successfully!")
    
    elif choice == "4":
        # Gracefully exit the program when the user selects the quit option
        print("Goodbye! Have a great day!")
        break  

    else:
        # Notify the user if they enter an invalid choice and prompt them again
        print("Invalid choice! Please enter a number between 1 and 4.")

