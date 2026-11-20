
import subprocess

# Test 1: Hardcoded password
DATABASE_PASSWORD = "admin123"

def connect_database():
    print("Connecting to database")

# Test 2: Command injection vulnerability
def run_command(user_input):
    subprocess.call(user_input, shell=True)

# Test 3: Unused variable
def calculate_total():
    unused_value = 100
    return 50

if __name__ == "__main__":
    connect_database()
    run_command("echo Hello")
    print(calculate_total())
