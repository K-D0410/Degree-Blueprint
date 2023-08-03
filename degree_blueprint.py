import nicknames_to_major as nnm
import majors_info

print("Welcome to the Degree Blueprint project!")
print("This project provides 4-year plans based on the catalog year 2022-2023 for the University of Connecticut.")

while True:
    # Get user's Major choice
    major_choice = input("Please enter your major choice: ")

    # Clean and standardize the major choice to lowercase
    major_choice = major_choice.lower()

    # Check if the major is available in the dictionary
    if major_choice in nnm.nicknames_to_major:
        # Resolve nicknames or abbreviations to official major names
        major_choice = nnm.nicknames_to_major[major_choice]
        break  # Exit the loop if the major choice is valid
    else:
        # Display a personalized note for majors not available
        print(f"Sorry, information for the major '{major_choice}' is not available yet.")
        print("Please check back later or select another major.\n")

# Get user's BA/BS selection
ba_bs_choice = input("Please choose between Bachelor of Arts (BA) or Bachelor of Science (BS): ")

# Clean and standardize the BA/BS choice to uppercase
ba_bs_choice = ba_bs_choice.upper()

# Check if the major is available in the majors_info dictionary
if major_choice in majors_info.majors_info:
    # Get school and credits information based on the major and BA/BS choice
    school = majors_info.majors_info[major_choice]['school']
    credits_needed = majors_info.majors_info[major_choice][ba_bs_choice]

    # Check if the selected degree type is offered for the major
    if credits_needed is not None:
        # Display the information to the user
        print(f"{major_choice} ({ba_bs_choice}) - {school}")
        print(f"{credits_needed} credits needed to graduate")
    else:
        # Display a message indicating that the selected degree is not offered
        print(f"Sorry, a {ba_bs_choice} degree is not offered for {major_choice}.")

    # Provide the link to the Google Spreadsheet
    print("\nVisit (google spreadsheet link) and click on your major to bring you to a more detailed plan")

else:
    # Display a personalized note for majors not available in nicknames_to_major
    print(f"Sorry, information for the major '{major_choice}' is not available yet.")
    print("Please check back later or enter another major.\n")
