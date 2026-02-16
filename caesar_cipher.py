ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()'

def caesar_cipher(message, key, mode):
    result = ""
    for char in message:
        if char in ALPHABET:
            current_index = ALPHABET.find(char)
            if mode == 'encrypt':
                new_index = (current_index + key) % len(ALPHABET)
            else: # decrypt
                new_index = (current_index - key) % len(ALPHABET)
            result += ALPHABET[new_index]
        else:
            result += char
    return result

def get_valid_mode():
    """Forces user to enter 'encrypt' or 'decrypt'."""
    while True:
        user_input = input("Select Mode (encrypt/decrypt): ").lower().strip()
        if user_input in ['encrypt', 'e']:
            return 'encrypt'
        elif user_input in ['decrypt', 'd']:
            return 'decrypt'
        else:
            print("❌ Invalid mode. Please type 'encrypt' or 'decrypt'.")

def get_valid_key():
    """Forces user to enter a valid integer number."""
    while True:
        user_input = input("Enter shift key (number): ").strip()
        try:
            val = int(user_input)
            return val
        except ValueError:
            print("❌ Invalid key. Please enter a whole number (e.g., 3, 5, 10).")

def get_valid_message():
    """Forces user to enter a non-empty message."""
    while True:
        msg = input("Enter the message: ").strip()
        if len(msg) > 0:
            return msg
        else:
            print("❌ Message cannot be empty. Please type something.")



def main():
    print("--- Caesar Cipher  ---")
    mode = get_valid_mode()
    message = get_valid_message()
    key = get_valid_key()
    output = caesar_cipher(message, key, mode)
    
    print("\n" + "="*30)
    print(f"✅ OPERATION SUCCESSFUL")
    print(f"Mode:   {mode.upper()}")
    print(f"Result: {output}")
    print("="*30)

if __name__ == "__main__":
    main()
