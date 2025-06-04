import secrets
import string


def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    character_pool = ''
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("No character types selected")

    return ''.join(secrets.choice(character_pool) for _ in range(length))


def main():
    try:
        length = int(input('Password length: '))
    except ValueError:
        print('Invalid length')
        return

    use_lowercase = input('Include lowercase letters? (y/n): ').strip().lower() == 'y'
    use_uppercase = input('Include uppercase letters? (y/n): ').strip().lower() == 'y'
    use_digits = input('Include digits? (y/n): ').strip().lower() == 'y'
    use_symbols = input('Include symbols? (y/n): ').strip().lower() == 'y'

    try:
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
        print('Generated password:', password)
    except ValueError as e:
        print('Error:', e)


if __name__ == '__main__':
    main()
