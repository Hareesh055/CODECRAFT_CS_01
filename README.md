**🔐 Caesar Cipher Implementation**

A Python implementation of the classical Caesar Cipher algorithm for encrypting and decrypting text.

**📖 About**

This project implements the Caesar Cipher, one of the earliest and simplest substitution ciphers in cryptography.

In this method, each letter in a message is shifted by a fixed number of positions in the alphabet using a key value. The technique is historically associated with Julius Caesar, who reportedly used it to protect confidential military communication.

Although not secure by modern standards, this cipher provides a strong foundation for understanding basic encryption principles.

**🎯 Objective**

The objective of this project is to:

Implement the Caesar Cipher algorithm in Python

Allow users to encrypt and decrypt messages

Accept a user defined shift key

Demonstrate fundamental data protection concepts

Present the implementation in a structured and documented format

**✨ Features**

User friendly command line interface

Supports both encryption and decryption modes

Accepts custom shift values

Preserves uppercase and lowercase letters

Keeps non alphabet characters unchanged

Uses modulo arithmetic for wrap around logic

**⚙️ How the Algorithm Works**

The user selects a mode (Encrypt or Decrypt).

The user enters a message and a shift key.

Each alphabet character is converted to its position index.

The character position is shifted forward (encryption) or backward (decryption).

Modulo operation ensures circular shifting within alphabet range.

The final transformed message is displayed.

**🧠 Example**

Input
Message: HELLO
Key: 3
Mode: Encrypt

Output
KHOOR


**📚 Learning Outcomes**

Understanding of classical substitution ciphers

Implementation of encryption logic using Python

Use of modular arithmetic in programming

Practical exposure to basic security concepts

Structured project documentation

**✅ Conclusion**

This project successfully demonstrates the working of the Caesar Cipher algorithm through a fully functional Python implementation. It serves as a foundational step towards understanding more advanced cryptographic techniques and secure system development.
