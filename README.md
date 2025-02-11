# Password Complexity Checker

A Python-based tool to assess the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. The tool provides feedback to users on the password's strength and offers suggestions for improvement.

---

### Features

- **Password Strength Assessment**:
  - Evaluates passwords based on a scoring system.
  - Categorizes passwords as **Weak**, **Moderate**, or **Strong**.
- **Detailed Feedback**:
  - Provides specific suggestions for improving password strength (e.g., adding uppercase letters, numbers, or special characters).
- **Customizable Criteria**:
  - Adjustable weights for length, character types, and special characters to suit specific security requirements.
- **Simple and Intuitive**:
  - Command-line interface for easy use.
  - Clear and concise output for quick understanding.

---

### How It Works

The tool checks the following criteria to determine password strength:
1. **Length**: Passwords should be at least 8 characters long (12+ for higher security).
2. **Character Diversity**:
   - Uppercase letters (`A-Z`).
   - Lowercase letters (`a-z`).
   - Numbers (`0-9`).
   - Special characters (`!@#$%^&*(),.?":{}|<>`).
3. **Scoring System**:
   - Each criterion contributes to a strength score.
   - The final score determines the password's strength level.

---

### Example Output

```
Enter your password: Sahil123!
Password Strength: Strong
Feedback:
- Your password meets all recommended criteria.
```

```
Enter your password: sahil
Password Strength: Weak
Feedback:
- Password should be at least 8 characters long.
- Password should contain at least one uppercase letter.
- Password should contain at least one number.
- Password should contain at least one special character.
```
