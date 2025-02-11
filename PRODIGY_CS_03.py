import re
def check_password_strength(password):
    strength_score = 0
    length_weight = 1
    uppercase_weight = 1
    lowercase_weight = 1
    number_weight = 1
    special_char_weight = 2
    
    if len(password) >= 8:
        strength_score += length_weight
    if len(password) >= 12:
        strength_score += length_weight
    if re.search(r'[A-Z]', password):
        strength_score += uppercase_weight
    if re.search(r'[a-z]', password):
        strength_score += lowercase_weight
    if re.search(r'[0-9]', password):
        strength_score += number_weight
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += special_char_weight
    if strength_score >= 6:
        strength_level = "Strong"
    elif strength_score >= 4:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"
    
    feedback = []
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    if not re.search(r'[0-9]', password):
        feedback.append("Password should contain at least one number.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password should contain at least one special character.")
    return strength_level, feedback

def main():
    password = input("Enter your password: ")
    strength_level, feedback = check_password_strength(password)
    print(f"Password Strength: {strength_level}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")
if __name__ == "__main__":
    main()