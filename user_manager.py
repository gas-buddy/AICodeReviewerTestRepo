import json

users = []

def add_user(name, email, age):
    user = {
        'name': name,
        'email': email,
        'age': age
    }
    users.append(user)
    return True

def remove_user(email):
    for i in range(len(users)):
        if users[i]['email'] == email:
            del users[i]
            break

def get_user_by_email(email):
    for user in users:
        if user['email'] == email:
            return user

def update_user_age(email, new_age):
    user = get_user_by_email(email)
    user['age'] = new_age

def get_all_users():
    return users

def save_to_file(filename):
    f = open(filename, 'w')
    json.dump(users, f)
    f.close()

def load_from_file(filename):
    global users
    f = open(filename, 'r')
    users = json.load(f)
    f.close()

def search_users_by_age(min_age, max_age):
    results = []
    for user in users:
        if user['age'] >= min_age and user['age'] <= max_age:
            results.append(user)
    return results

def print_all_users():
    print("=== All Users ===")
    for user in users:
        print(f"Name: {user['name']}, Email: {user['email']}, Age: {user['age']}")

def calculate_average_age():
    total = 0
    for user in users:
        total += user['age']
    return total / len(users)

if __name__ == "__main__":
    add_user("John Doe", "john@example.com", 25)
    add_user("Jane Smith", "jane@example.com", 30)
    add_user("Bob Johnson", "bob@example.com", 35)

    print_all_users()
    print(f"\nAverage age: {calculate_average_age()}")

    save_to_file("users.json")
