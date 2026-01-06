#!/usr/bin/env python3

import sys
import os


def otp_crypt(input_file, key_file, output_file):
    """Encrypts/Decrypts a file using a One-Time Pad (OTP) encryption and truncates the used key."""

    # Check the sizes of the input file and the key file
    input_size = os.path.getsize(input_file)
    key_size = os.path.getsize(key_file)

    if key_size < input_size:
        print(
            f"Error: Key file '{key_file}' is too short.")
        sys.exit(1)

    try:
        with open(input_file, 'rb') as inf, open(key_file, 'rb+') as kf, open(output_file, 'wb') as of:
            while True:
                # Read one byte at a time from the input and key
                input_byte = inf.read(1)
                key_byte = kf.read(1)

                # Stop if we've reached the end of the file
                if not input_byte:
                    break

                # XOR the input byte with the key byte
                encrypted_byte = bytes([input_byte[0] ^ key_byte[0]])

                # Write the encrypted/decrypted byte to the output file
                of.write(encrypted_byte)

        print(f"Completed: {output_file}")

        # Truncate the key file by removing the used portion
        truncate_key_file(key_file, input_size)

    except Exception as e:
        print(f"Error during operation: {e}")


def truncate_key_file(key_file, used_size):
    """Truncates the key file by removing the used portion."""
    try:
        with open(key_file, 'rb+') as kf:
            # Move the file pointer to the end of the used portion
            kf.seek(used_size)

            # Read the remaining key data
            remaining_key = kf.read()

            # Truncate the file and write the remaining key data back
            kf.seek(0)
            kf.write(remaining_key)
            kf.truncate()  # Truncate the file to the new size (removing the used part)

        print(f"Key file '{key_file}' truncated by {used_size} bytes.")

    except Exception as e:
        print(f"Error while truncating key file: {e}")


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <input_file> <key_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    key_file = sys.argv[2]
    output_file = sys.argv[3]

    otp_crypt(input_file, key_file, output_file)


if __name__ == "__main__":
    main()
