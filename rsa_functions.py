from number_theory_functions import *

class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        p = generate_prime(digits // 2 + 1)
        q = generate_prime(digits// 2 + 1)
        N = p * q
        fi_N = (p-1) * (q-1)
        for i in range(2, fi_N):
            if extended_gcd(fi_N, i)[0] is 1:
                public = i
                break
        private = modular_inverse(public, fi_N)
        return RSA((N, public), (N, private))
    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        (N , e) = self.public_key
        return modular_exponent(m, e, N)


    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        (N , d) = self.private_key
        return modular_exponent(c, d, N)
