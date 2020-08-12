# its350
course materials and references for its350

## Lab07: Digital Signature

__Description__

Based on the combinations of encryption/decryption/signing/verification/digest, many communication protocols can be designed. In this lab, you will carry out two protocols then compare them:

* Encrypt-then-sign
* Sign-then-encrypt

Find a classmate as your communication partner, complete Task 2 and 3 below collaboratively, but complete Task 1 and 4 by yourself. Name all the files properly with your first name and your partner's first name. For example, the message send from Alice to Bob can be named as 'Message\_Alice2Bob' or simply 'mA2B'.

__Task 1: Create a pair of asymmetric keys (10%)__

In this task, complete the following steps:

  1. Generate a pair of RSA private/public keys, protect your private key with a secret password known only to yourself
  2. Email your public key to your partner
  3. Create a short message <!-- $ M : $ --> <img style="transform: translateY(0.25em);" src="../../svg/TkgA9uCEN8.svg"/> 'Message from YourName to Your partner's name', for example, <!-- $ M : $ --> <img style="transform: translateY(0.25em);" src="../../svg/TkgA9uCEN8.svg"/> 'Message from Alice to Bob'
	

__Task 2: Encrypt-then-sign (35%)__

In this task, complete the following steps:

  1. __Encrypt__ <!-- $ M : $ --> <img style="transform: translateY(0.25em);" src="../../svg/TkgA9uCEN8.svg"/> with your partner's public key, and get the ciphertext <!-- $ C $ --> <img style="transform: translateY(0.25em);" src="../../svg/AsaAIYPtwM.svg"/>
  2. __Sign__ <!-- $ C $ --> <img style="transform: translateY(0.25em);" src="../../svg/AsaAIYPtwM.svg"/> with your private key (choose sha256 as the digest), and get the signature <!-- $ S $ --> <img style="transform: translateY(0.25em);" src="../../svg/dWhO5fpKHV.svg"/>
  3. Email both <!-- $ C $ --> <img style="transform: translateY(0.25em);" src="../../svg/AsaAIYPtwM.svg"/> and <!-- $ S $ --> <img style="transform: translateY(0.25em);" src="../../svg/dWhO5fpKHV.svg"/> to your partner
  4. Verify the <!-- $ S' $ --> <img style="transform: translateY(0.25em);" src="../../svg/2zXazcu5qH.svg"/> you received with your partner's public key against the <!-- $ C' $ --> <img style="transform: translateY(0.25em);" src="../../svg/gIOqrGbqIJ.svg"/> you received to check the authenticity and integrity of <!-- $ C' $ --> <img style="transform: translateY(0.25em);" src="../../svg/gIOqrGbqIJ.svg"/>
  5. Decrypt the <!-- $ C' $ --> <img style="transform: translateY(0.25em);" src="../../svg/gIOqrGbqIJ.svg"/> you received with your private key, and get the message <!-- $ M' $ --> <img style="transform: translateY(0.25em);" src="../../svg/WVbQy3VEg5.svg"/>



__Task 3: Sign-then-encrypt (35%)__

In this task, complete the following steps:

  1. __Sign__ <!-- $ M $ --> <img style="transform: translateY(0.25em);" src="../../svg/Cz6uMB1L2n.svg"/> with your private key, and get the signature <!-- $ S $ --> <img style="transform: translateY(0.25em);" src="../../svg/dWhO5fpKHV.svg"/>
  2. __Encrypt__ <!-- $ M $ --> <img style="transform: translateY(0.25em);" src="../../svg/Cz6uMB1L2n.svg"/> with your partner's public key, and get the ciphertext <!-- $ C $ --> <img style="transform: translateY(0.25em);" src="../../svg/AsaAIYPtwM.svg"/>
  3. Email both <!-- $ C $ --> <img style="transform: translateY(0.25em);" src="../../svg/AsaAIYPtwM.svg"/> and <!-- $ S $ --> <img style="transform: translateY(0.25em);" src="../../svg/dWhO5fpKHV.svg"/> to your partner
  4. Decrypt the <!-- $ C' $ --> <img style="transform: translateY(0.25em);" src="../../svg/gIOqrGbqIJ.svg"/> you received with your private key, and get the message <!-- $ M' $ --> <img style="transform: translateY(0.25em);" src="../../svg/WVbQy3VEg5.svg"/>
  5. Verify the <!-- $ S' $ --> <img style="transform: translateY(0.25em);" src="../../svg/2zXazcu5qH.svg"/> you received with your partner's public key against the <!-- $ M' $ --> <img style="transform: translateY(0.25em);" src="../../svg/WVbQy3VEg5.svg"/> you get in the previous step to check the authenticity and integrity of <!-- $ M' $ --> <img style="transform: translateY(0.25em);" src="../../svg/WVbQy3VEg5.svg"/>


__Task 4: Comparison (20%)__

Answer the following questions and justify your solutions.


  1. Can 'encrypt-then-sign' assure integrity, authenticity, non-repudiation and confidentiality?
  2. Can 'sign-then-encrypt' assure integrity, authenticity, non-repudiation and confidentiality?
  3. Can the sender be spoofed by the receiver in 'encrypt-then-sign'?
  4. Can the sender be spoofed by the receiver in 'sign-then-encrypt'?


__Report__

Write a report about the process you complete the tasks in the description, key screen snapshots are needed as evidences.


__References__
* [Should we sign-then-encrypt, or encrypt-then-sign?](https://crypto.stackexchange.com/questions/5458/should-we-sign-then-encrypt-or-encrypt-then-sign)
* [Cryptography Digital signatures.](https://www.tutorialspoint.com/cryptography/cryptography\_digital\_signatures.htm)
* [Defective Sign-and-Encrypt](http://www.drdobbs.com/defective-sign-and-encrypt/184404841)
* [Defective Sign & Encrypt in S/MIME, 	PKCS\#7, MOSS, PEM, PGP, and XML.](http://world.std.com/~dtd/sign\_encrypt/sign\_encrypt7.html)
* [The Order of Encryption and Authentication for Protecting Communications.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.5488&rep=rep1&type=pdf)
* [Authenticated Encryption: Relations among notions and analysis of the generic composition paradigm.](./papers/oem.pdf)
	