import random
import string
import argparse
from typing import List

class PasswordGenerator:
    """A customizable password generator with multiple complexity options"""
    
    def __init__(self):
        self.lower = string.ascii_lowercase
        self.upper = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_-+=<>?"
    
    def generate_password(self, length: int = 12, use_upper: bool = True, 
                         use_digits: bool = True, use_symbols: bool = True) -> str:
        """Generate a random password with specified complexity"""
        chars = self.lower
        if use_upper:
            chars += self.upper
        if use_digits:
            chars += self.digits
        if use_symbols:
            chars += self.symbols
        
        password = []
        for _ in range(length):
            password.append(random.choice(chars))
        
        random.shuffle(password)
        return ''.join(password)

def save_to_file(passwords: List[str], filename: str = "passwords.txt") -> None:
    """Save generated passwords to a text file"""
    with open(filename, "w") as f:
        f.write("\n".join(passwords))
    print(f"Saved passwords to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Random Password Generator")
    parser.add_argument("-n", "--number", type=int, default=5, help="Number of passwords to generate")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length")
    parser.add_argument("--no-upper", action="store_false", dest="use_upper", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_false", dest="use_digits", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_false", dest="use_symbols", help="Exclude symbols")
    parser.add_argument("-o", "--output", help="Output file to save passwords")
    
    args = parser.parse_args()
    
    generator = PasswordGenerator()
    passwords = [generator.generate_password(
        length=args.length,
        use_upper=args.use_upper,
        use_digits=args.use_digits,
        use_symbols=args.use_symbols
    ) for _ in range(args.number)]
    
    print("\n".join(passwords))
    
    if args.output:
        save_to_file(passwords, args.output)

if __name__ == "__main__":
    main()
