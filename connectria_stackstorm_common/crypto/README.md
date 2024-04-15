# Crypto Library

## Description
This library provides encryption and decryption functionalities for StackStorm packs.

## Usage

```python
from connectria_stackstorm_common.crypto import CryptoLib

crypto = CryptoLib()

encrypted_message = crypto.encrypt("Hello World")
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = crypto.decrypt(encrypted_message)
print(f"Decrypted Message: {decrypted_message}")
