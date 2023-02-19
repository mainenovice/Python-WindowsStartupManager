import subprocess

# Run PowerShell command to retrieve list of startup programs
startup_command = "Get-CimInstance -Class Win32_StartupCommand"
startup_process = subprocess.Popen(["powershell", startup_command], stdout=subprocess.PIPE)
startup_output = startup_process.communicate()[0]

# Parse the output and put each startup program in a list
startup_list = startup_output.decode("utf-8").strip().split('\n')

# Print each item with its index value
for index, item in enumerate(startup_list):
    print(f"{index}: {item}")

# Get user input for the index of the program to remove
program_index = None
while program_index is None:
    try:
        program_index = int(input("Enter the index of the program to remove: "))
        if program_index < 0 or program_index >= len(startup_list):
            print("Invalid index value. Please enter a value between 0 and", len(startup_list) - 1)
            program_index = None
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        program_index = None

# Remove the selected startup program
remove_command = f"{startup_list[program_index]} | Remove-CimInstance"
subprocess.run(["powershell", remove_command])
