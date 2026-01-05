# Simple One-Time Pad (OTP) Tool

A Python implementation of a **One-Time Pad (OTP)** encryption/decryption tool.  
Encrypt or decrypt files with a key of the same size, demonstrating:

- XOR-based encryption
- File I/O in Python
- Secure key usage and truncation

---

## Features

- Encrypt or decrypt files with OTP
- Truncates used portion of the key to prevent reuse
- Easy CLI usage
- Educational and safe for small files

---

## Usage

### Encrypt/Decrypt a file

```bash
python otp.py <input_file> <key_file> <output_file>
