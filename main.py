import os

def add_tenant_note():
    tenant_name = input("Enter the tenant's name: ")
    apartment_number = input("Enter their apartment number: ")
    note_date = input("Enter the date (YYYY-MM-DD): ")
    wellness_check_type = input("What type of note is this? ")
    tenant_coordinator= input("Who is writing this note? ")
    wellness_check_note = input("Enter your Wellness check note: ")
    clean_name = tenant_name.replace(' ','_').lower()
    clean_date = note_date.replace('-','_')
    base_name = clean_date
    tenant_folder = os.path.join('notes', f"{clean_name}_{apartment_number}")
    os.makedirs(tenant_folder, exist_ok=True)
    files = os.listdir(tenant_folder)
    count = 0
    for file in files:
        if file.startswith(base_name):
            count += 1
    file_name = base_name + "_note" + str(count + 1) + ".txt"
    info = [
        ("Tenant name", tenant_name),
        ("Tenant Apartment", apartment_number),
        ("Date", note_date),
        ("Wellness check type", wellness_check_type),
        ("Tenant who completed this note", tenant_coordinator),
        ("Wellness check note", wellness_check_note)
    ]
    file_path = os.path.join(tenant_folder, file_name)
    with open(file_path, 'w') as file:
        for label, value in info:
            file.write(f'{label}: {value}\n')
    print(f'Saved note: {file_path}')


def view_tenant_note():
    pass


def exit_program():
    print('Goodbye!')
    exit()



print('Welcome to the Tenant Coordinator Program\n')

while True:
    print('1. Add Tenant Note\n2. View Tenant Notes\n3. Exit')
    
    user_choice = input('Please enter an option: ')

    if user_choice == '1':
        add_tenant_note()
    elif user_choice == '2':
        print("Coming soon")
    elif user_choice == '3':
        exit_program()
    else:
        print("Invalid choice please enter between 1 - 3")
