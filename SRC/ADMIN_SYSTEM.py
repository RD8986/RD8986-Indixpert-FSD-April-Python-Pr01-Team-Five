import os
from SRC.COLORS import Colors

class AdminSystem:
    def __init__(self, auth_system):
        self.auth_system = auth_system

    def delete_user(self, admin, username):
        if admin.role == 'Admin':
            if username in self.auth_system.users and username != admin.username:
                del self.auth_system.users[username]
                self.auth_system.save_users()
                print(Colors.OKGREEN + f"User {username} deleted by {admin.first_name}." + Colors.ENDC)
            elif username == admin.username:
                print(Colors.FAIL + "You cannot delete yourself." + Colors.ENDC)
            else:
                print(Colors.FAIL + f"User {username} not found." + Colors.ENDC)
        else:
            print(Colors.FAIL + "Only Admins can delete users." + Colors.ENDC)

    def replace_admin(self, admin, new_username):
        if new_username in self.auth_system.users and self.auth_system.users[new_username]['role'] == 'User':
            self.auth_system.users[new_username]['role'] = 'Admin'
            self.auth_system.users[admin.username]['role'] = 'User'
            self.auth_system.admin_username = new_username
            self.auth_system.save_users()
            print(Colors.OKGREEN + f"Admin replaced by {new_username}." + Colors.ENDC)
        else:
            print(Colors.FAIL + "User not found or not eligible to be an admin." + Colors.ENDC)

    def view_error_logs(self):
        if os.path.exists('database/exception_log.json'):
            with open('database/exception_log.json', "r") as log_file:
                print(Colors.OKCYAN + "Error Log:" + Colors.ENDC)
                print("------------------------------------------------------")
                for line in log_file:
                    print(line.strip())
                print("------------------------------------------------------")
        else:
            print(Colors.WARNING + "No error logs found." + Colors.ENDC)
