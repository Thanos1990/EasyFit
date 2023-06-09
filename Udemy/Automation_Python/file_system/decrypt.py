from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA


def decrypt(key, passphrase, encrypted_file_path):
    print("Decrypting file {} ...".format(encrypted_file_path))
    rsa_key = RSA.import_key(key, passphrase=passphrase)
    with open(encrypted_file_path, 'rb') as f:
        # Read the encoded session key, nonce, digest and encrypted data
        enc_session_key, nonce, digest, ciphertext = \
        [f.read(x) for x in (rsa_key.size_in_bytes(),16,16,-1)]

        # decode the session key
        cipher_rsa = PKCS1_OAEP.new(rsa_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)

        # finally decrypt data
        data = cipher_aes.decrypt_and_verify(ciphertext, digest)
        print('Done')
        return data


if __name__ == '__main__':
    # decrypting needs the private RSA key
    with open('private.rsa', 'rb') as g:
        private_key = g.read()
        plain_data = decrypt(private_key, 'supersecret', 'encryptedmyfile.bin')
        print('Decrypted data:\n')
        print(plain_data)