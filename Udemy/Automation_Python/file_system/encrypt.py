from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes


def encrypt(key, src_file_path, encrypted_file_path):
    print("Encrypting file {} to {} using AES".format(src_file_path,
                                                       encrypted_file_path))
    rsa_key = RSA.import_key(key)
    with open(encrypted_file_path, "wb") as outfile:
        # Create a random session key and encrypt it with the input RSA key
        session_key = get_random_bytes(16)
        cipher_rsa = PKCS1_OAEP.new(rsa_key)
        outfile.write(cipher_rsa.encrypt(session_key))

        # Create an AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)

        with open(src_file_path, 'rb') as infile:
            # Use AES session key to encrypt input file data
            data = infile.read()
            ciphertext, digest = cipher_aes.encrypt_and_digest(data)

            # write to target file
            outfile.write(cipher_aes.nonce)
            outfile.write(digest)
            outfile.write(ciphertext)
    print('Done')


if __name__ == '__main__':
    # we encrypt with a public key
    with open('public.pem', 'rb') as f:
        public_key = f.read()
        encrypt(public_key, 'myfile4.txt', 'encryptedmyfile.bin')

