# Simple One-Time Pad (OTP) Tool

A Python implementation of a One-Time Pad (OTP) encryption/decryption tool.  
Encrypt or decrypt files with a large enough key that gets automatically truncated.

---

## Usage

Encrypt/Decrypt a file:

```bash
python3 simple-otp/main.py <input_file> <key_file> <output_file>
```

Since the keyfile gets truncated there should be two copies. One at the sending and one at the recieving end.

--

## License

[MIT](https://choosealicense.com/licenses/mit/) 

