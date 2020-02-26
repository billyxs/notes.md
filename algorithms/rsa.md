# RSA algorithm 

Rivert, Shamir, Adleman

- [RSA classroom - pt 1 - YouTube](https://www.youtube.com/watch?v=4zahvcJ9glg)
- [RSA classroom - pt 2 - YouTube](https://www.youtube.com/watch?v=oOcTVTpUsPQ)

- [How RSA encryption works - YouTube](https://www.youtube.com/watch?v=Z8M2BTscoD4)


Devloped in 1977

Allowed encryption and decryption with separate keys


Encrypt
m<sup>e</sup> mod n = c


Decrypt
c<sup>d</sup> mod n = m

(m<sup>e</sup> mod n)d mod n = m


Private key = e and n
Public key = d


"One-way trapdoor function"
There's no way to undo the encryption function unless you know the trapdoor
n is the trapdoor


Use Prime factorization

Fundamental theorem of arithmetic

Any number greater than 1 can be written in exactly one way as a product of prime numbers.
