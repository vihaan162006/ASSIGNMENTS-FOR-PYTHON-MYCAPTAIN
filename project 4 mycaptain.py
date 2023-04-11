import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "Email ID"])
        
        writer.writerow(info_list)

def add_student_info():
    student_info_list = []
    print("Please enter the student's information:")
    name = input("Name: ")
    age = input("Age: ")
    contact_number = input("Contact Number: ")
    email_id = input("Email ID: ")
    student_info_list.append(name)
    student_info_list.append(age)
    student_info_list.append(contact_number)
    student_info_list.append(email_id)
    write_into_csv(student_info_list)
    print("Student information has been added successfully.")

def get_student_info(name):
    with open('student_info.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        
        for row in reader:
            if row[0] == name:
                print(f"Name: {row[0]}\nAge: {row[1]}\nContact Number: {row[2]}\nEmail ID: {row[3]}")
                return
        print("Student not found.")

def main():
    choice = ""
    while choice != "3":
        print("Please select an option:")
        print("1. Add student information")
        print("2. Get student information")
        print("3. Exit")
        choice = input("Choice: ")
        
        if choice == "1":
            add_student_info()
        elif choice == "2":
            name = input("Please enter the student's name: ")
            get_student_info(name)
        elif choice == "3":
            print("Exiting program...")
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
    
