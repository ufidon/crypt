# its350
course materials and references for its350

## Lab08: Public Key Infrastructure

__Description__

Early HTTP websites suffer from  eavesdropping and tampering during the communication by man-in-the-middle attacks. By using [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport\_Layer\_Security), or its predecessor, Secure Sockets Layer (SSL), those attacks are mitigated. The secured HTTP protocol, denoted as [HTTPS](https://en.wikipedia.org/wiki/HTTPS), is often called as HTTP over TLS, or HTTP over SSL.
	
The corner stone of TLS/SSL is public cryptography and PKI. In this lab, an adaption from [SEED Public-Key Infrasturcture (PKI) Lab](https://seedsecuritylabs.org/Labs\_16.04/Crypto/Crypto\_PKI/) Task 2&3, you will set up a HTTPS website and test it using your public key certificate  and your private key. 

The website to be secured is _YourFirstNameYourLastName.its350.edu_, e.g. _BillClinton.its350.edu_. In your certificate signing request, the Common Name(CN) should be _YourFirstNameYourLastName.its350.edu_.
	
__Task 1: Obtaining a Certificate (40%)__

* Step 1: _Generate public/private key pair._ Run the following commands to generate a RSA key pair (both private and public keys) for your website. Name your key files as _YourFirstNameYourLastName.pri_ and _YourFirstNameYourLastName.pub_ respectively. Then check the actual content, such as the modulus, private exponents, etc. e.g.

```bash
# 1. generate private key
openssl genrsa  -out BillClinton.pri 2048
# 2. generate public key
openssl rsa -in BillClinton.pri -pubout -out BillClinton.pub
# 3. check the actual content of the private key
openssl rsa -in BillClinton.pri -text -noout
# 4. check the actual content of the public key
openssl rsa -in BillClinton.pub -pubin -text -noout
```


* Step 2: _Generate a Certificate Signing Request (CSR)_. The CSR includes your public key. It will be sent to the CA. The CA will generate a certificate for your public key (usually after ensuring that identity information in the CSR matches with the website’s true identity, i.e. FQDN, fully qualified domain name). Please fill the following information in your certificate signing request:

Field | Value
------|------
E(Email) 							| your pnw email
CN(Common Name) 			| _YourFirstNameYourLastName.its350.edu_
OU(Organization Unit) | Westville campus 
O(Organization Name) 	| Purdue University Northwest 
L(Location Name) 			| Westville 
S(State Name) 				| Indiana 
C(Country Name) 			| US 


_Note: No challenge password or optional company name above._


For example,

Field | Value
------|------
E(Email) 							| bill123@pnw.edu 
CN(Common Name) 			| BillClinton.its350.edu
OU(Organization Unit) | Westville campus 
O(Organization Name) 	| Purdue University Northwest 
L(Location Name) 			| Westville 
S(State Name) 				| Indiana 
C(Country Name) 			| US 


The command for generating the CSR:

```bash
# 5. Generate a certifcate from an existent private key
openssl req -new -key BillClinton.pri -out BillClinton.csr
```

* Step 3: _Generating Certificates._ The CSR file needs to have a CA’s signature to form a certificate. In the real world, the CSR files are usually sent to a trusted CA for their signature. In this lab, you serve as a trusted CA to generate certificates. The following command turns the certificate signing request
(BillClinton.csr) into an X509 certificate (BillClinton.crt),  download [pki.7z](./pki/pki.7z)  and extract it to get a pki folder, copy your csr file into the folder pki/ca/req, cd into ca folder, run the command below to generate the certificate(password: P@ssw0rd):

```bash
# 6. Sign a certificate signing request to 
# turn it into an X509 certificate
openssl ca -cert ca.crt  -keyfile ca.key -config openssl.cnf -in req/BillClinton.csr -out crts/BillClinton.crt 
```


* Step 4: _Verifying Certificates._  Copy the CA's certificate ca.crt  from folder pki/ca and your certificate from pki/ca/crts to the same folder as your private key's. Run the following command to verify CA's signature on your certificate.


```bash
# 7. Verify the CA's signature on your X509 certificate
openssl verify -CAfile ca.crt BillClinton.crt
```


__Task 2: Deploying Certificate in an HTTPS Web Server (60%)__

In this lab, you will explore how public-key certificates are used by websites to secure website-browser communication. you will set up an HTTPS website using openssl’s built-in web server.


* Step 1: _Configuring DNS._ Choose the FQDN, YourFirstNameYourLastName.its350.edu, in your certificate as the name of your website. To get your VM recognize this name, add the following entry or line to the end of /etc/hosts using subl; this entry basically maps your FQDN to the localhost (i.e., 127.0.0.1):


```bash
# 1. open /etc/hosts in subl
sudo subl /etc/hosts
# 2. add the following entry or line to the end of /etc/hosts
127.0.0.1     _YourFirstNameYourLastName.its350.edu_
```

* Step 2: _Configuring the web server._ Launch a simple web server with your certificate. OpenSSL allows you to start a simple web server using the  s\_server  command:

```bash
# 9. Combine your secret key and your certificate into one file
cp BillClinton.pri server.pem
cat BillClinton.crt >> server.pem
# 10. Launch the web server certified by server.pem
openssl s_server -cert server.pem -accept 443 -www
```

By default, the server will listen on port 4433, which is not the default HTTPS port number 443. We alter that using the -accept 443 option. Now, you can access the server by typing the following URL in Firefox's address box: 

```bash
# 11. Browse your website secured with HTTPS
https://YourFirstNameYourLastName.its350.edu/
``` 
Most likely, you will get an error message from the browser. In Firefox, you will see a message like the following:

```bash
“YourFirstNameYourLastName.its350.edu uses an invalid security certificate. The certificate is not trusted because the issuer certificate is unknown”.
```

* Step 3: _Setting the browser to accept our CA certificate._ Had our certificate been assigned by a public CA such as InCommon Federation, we will not have such an error message, because InCommon’s certificate is very likely preloaded into Firefox’s certificate repository already. Unfortunately, your certificate of 'YourFirstNameYourLastName.its350.edu' is signed by the class-scope CA, you used a self-signed certificate, and this CA is not recognized by Firefox. There are two ways to get Firefox to accept our CA’s self-signed certificate.


  * We can request Mozilla to include our CA’s certificate in its Firefox software, so everybody using Firefox can recognize our CA. This is how the real CAs, such as InCommon, get their certificates into Firefox. Unfortunately, our own CA does not have a large enough market for Mozilla to include our certificate, so we will not pursue this direction.
  * Load ca.crt into Firefox: We can manually add our CA’s certificate to the Firefox browser by clicking the Preferences menu then Find 'certificate' in Preferences, then click 'view certificates'. 	You will see a list of authority certificates that are already accepted by Firefox. From here, we can “import” our own CA certificate. Please import ca.crt, and select the following option: “Trust this CA to identify web sites”. You will see that our CA’s certificate is now in Firefox’s list of the accepted certificates.
  * You might want to intall our ca.crt on the SEED VM following [How do I install a root certificate?](https://askubuntu.com/questions/73287/how-do-i-install-a-root-certificate) which is excerpted here 
	

```bash
# 1. Create a directory for extra CA certificates in 
# /usr/share/ca-certificates:
sudo mkdir /usr/share/ca-certificates/extra
# 2. Copy the CA .crt file to this directory:
sudo cp ca.crt /usr/share/ca-certificates/extra/ca.crt
# 3. Let Ubuntu add the .crt file's path relative to
# /usr/share/ca-certificates to /etc/ca-certificates.conf:
sudo dpkg-reconfigure ca-certificates
# To do this non-interactively, run:
sudo update-ca-certificates
# In case of a .pem file on Ubuntu, it must first be 
# converted to a .crt file:
openssl x509 -in ca.pem -inform PEM -out ca.crt
```

* Step 4. _Testing your HTTPS website._ Now, point the browser to

 https://YourFirstNameYourLastName.its350.edu. Please describe and explain your observations. 

Please also do the following tasks:

  1. Pay attention to 'SSL-Session:' on the web page and compare it with the manual steps your have done in Lab05
  2. Check your digital certificate from the locker icon at the left side of your website address in the address box of the browser and find its _chain of trust_
  3. How is you digital certificate verified automatically by the browser?
  <!--4. Make a copy of server.pem, then modify a single byte of server.pem using subl, and restart the server, and reload the URL (Repeat \textbf{Step 2}). What do you observe? Make sure you restore the original server.pem afterward. Note: the server may not be able to restart if certain places of server.pem is corrupted; in that case, choose another place to modify.-->
  4. Since YourFirstNameYourLastName.its350.edu points to the localhost, if you use https://localhost instead,  you will be connecting to the same web server. Please do so, _describe and explain_ your observations.


__Report__

Write a report about the process you complete the tasks in the description, key screen snapshots are needed as evidences.

__Demo__
* [Public key infrastructure](https://youtu.be/nEgCHRrdGxI)

__References__

* [What is HTTPS?](https://www.instantssl.com/ssl-certificate-products/https.html)
* [HTTPS](https://en.wikipedia.org/wiki/HTTPS)
* [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport\_Layer\_Security)
* [SEED Public-Key Infrasturcture (PKI) Lab](https://seedsecuritylabs.org/Labs\_16.04/Crypto/Crypto\_PKI/)
* [How do I install a root certificate?](https://askubuntu.com/questions/73287/how-do-i-install-a-root-certificate)
* [OpenSSL Command-Line HOWTO](https://www.madboa.com/geek/openssl/)