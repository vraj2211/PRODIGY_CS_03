import re

def assess_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_character_criteria = bool(re.search(r'[\W_]', password))
    
    # Count the number of criteria met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_character_criteria])
    
    # Feedback on individual criteria
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_character_criteria:
        feedback.append("Password should include at least one special character.")
    
    # Determine strength based on the number of criteria met
    if criteria_met == 0:
        strength = "Very Weak"
    elif criteria_met == 1:
        strength = "Weak"
    elif criteria_met == 2:
        strength = "Moderate"
    elif criteria_met == 3:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    return strength, feedback

# Example usage:
password = input("Enter a password to check its strength: ")
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for comment in feedback:
        print(f"- {comment}")
