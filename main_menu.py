def suggest_field():
    name = input("Enter Student Name: ")
    percentage = float(input("Enter Percentage: "))
    background = input("Enter Background (Pre-Medical / Pre-Engineering / Commerce / Arts): ").lower()

    print(f"\n🎓 Field Suggestion for {name} ({background}, {percentage}%)")

    if background == "pre-medical":
        if percentage >= 80:
            print("Suggested Fields: MBBS, BDS")
        elif percentage >= 70:
            print("Suggested Fields: Pharm-D, Nursing")
        elif percentage >= 60:
            print("Suggested Fields: BS Biology, BS Chemistry")
        else:
            print("Suggested Fields: BA, BSc General")

    elif background == "pre-engineering":
        if percentage >= 80:
            print("Suggested Fields: BE (Software, Mechanical, Electrical)")
        elif percentage >= 70:
            print("Suggested Fields: BS Computer Science, Architecture")
        elif percentage >= 60:
            print("Suggested Fields: BS Math, BS Physics")
        else:
            print("Suggested Fields: BSc General")

    elif background == "commerce":
        if percentage >= 70:
            print("Suggested Fields: BBA, CA")
        elif percentage >= 60:
            print("Suggested Fields: B.Com, BS Accounting")
        else:
            print("Suggested Fields: BA General")

    elif background == "arts":
        if percentage >= 70:
            print("Suggested Fields: BS English, Psychology")
        elif percentage >= 60:
            print("Suggested Fields: BA, Media Studies")
        else:
            print("Suggested Fields: Diploma Programs")

    else:
        print("❌ Invalid Background")


def user():
    while True:
        print("\n--- Student Menu ---")
        print("1. View Profile")
        print("2. Check Attendance")
        print("3. Fee Status")
        print("4. Library Records")
        print("5. Logout")
        print("7. Admission: ")

        choice = input("Enter Your Choice: ")

        if choice == "1":
             print("📌 Student Profile:")
             print("Name: Rehmat")
             print("ID: 101")
        elif choice == "2":
            print("📅 Attendance: 85%")
        elif choice == "3":
            print("💰 Fee Status: Paid")
        elif choice == "4":
            print("📚 Library Books: 2 Issued")
        elif choice == "5":
            print("👋 Logout successful!")
            break
        else:
            print("❌ Invalid choice, try again.")


def student_login():
    username = input("Enter your username: ")
    password = input("Enter your Password: ")
    user_name = "rehmat"
    user_pass = "1234"


    if username == user_name and password == user_pass:
        user()
    else:
        print("❌ Invalid Email or Password!")

choice = int(input("Enter Your Choice: "))
if choice == 1:
    student_login()
elif choice == 2:
    suggest_field()
elif choice == 3:
    print("👋 Exiting...")
else:
    print("❌ Invalid choice!")
