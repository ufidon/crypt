# its350
course materials and references for its350

## Lab09: Application of Cryptography

### Description

The combination of modern symmetric cryptography, asymmetric cryptography and hash functions form the basis of secure Internet, secure Intranet, secure system and service as well as Blockchain, etc. by assuring their __confidentiality, integrity, authenticity and nonrepudiation, which leads to availability.__

This lab is supposed to be done on a SEED virtual machine.


#### Task 1: Git and GitHub (30%)

There are lots of open source projects hosted on Github. In this task, you will learn how to set up secure communication between you VM machine and Github.

* Step 1: Greate a Github user account on [Github](https://github.com/). 
* Step 2: Check whether git is installed on your SEED VM.
  
```bash
# check git installed or not
git version
# if not, install it
sudo apt install git
```

		
* Step 3: Setup ssh credentials.
```bash
# 1. Generate a new pair of SSH private/public key
# Follow the prompts, accept the default file location by pressing enter
# Protect the private key with a secure passphrase
ssh-keygen -t rsa -b 4096 -C "your_email@pnw.edu"

# 2. Add your  SSH private key to the ssh-agent
# 2.1 run the ssh-agent in the background
eval "$(ssh-agent -s)"

# 2.2 Add your SSH private key to the ssh-agent
# follow the prompt, enter your secure passphrase
ssh-add ~/.ssh/id_rsa
```

* Step 4: Copy your ssh public key to your Github account
	
```bash
# 1. Use subl to open your ssh public key file, 
# copy its content into clipboard:
subl ~/.ssh/id\_rsa.pub
```
then follow [this online tutorial](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account) add your public ssh key to your account on Github. With subl, xclip is not needed.
	
* Step 5:  Verify the ssh credential configuration

```bash
# 1. Connect to Github 
# follow the prompt, if you get a yes/no question, answer yes
ssh -T git@github.com
# If the setup is good, you will get message like
> Hi username! You've successfully authenticated, 
> but GitHub does not provide shell access.
```


For further information refer to the tutorial [Connecting to GitHub with SSH](https://help.github.com/en/articles/connecting-to-github-with-ssh).

	
#### Task 2: Secure e-mails and files using GnuPG (70%)
In this task, you will use GnuPG to manage your private/public keys, certificates and your friends' certificates. By which, you can secure e-mails, files and folders.

Get an overview about [GnuPG](https://en.wikipedia.org/wiki/GNU\_Privacy\_Guard) and the Ubuntu help document [GnuPrivacyGuard How to](https://help.ubuntu.com/community/GnuPrivacyGuardHowto).

##### 2.1 Data/program integrity assurance (20%)
GnuPG can be used to _verify data integrity_, take GnuPG as an example, complete the subtasks:

* Step 1: Download GnuPG _tarball_ and its _signature_ files from [its official website](https://gnupg.org/download/index.html), save them in the same folder.
* Step 2: Import GnuPG public key and verify the tarball's integrity. From [Gnupg signature key](https://gnupg.org/signature\_key.html) webpage, copy its current public key and save it in a file named gnupg.pub in the same folder as the downloaded tarball and signature files.

```bash
# 1. Inport GnuPG public key, 
gpg --import gnupg.pub 

# 2. verify the data integrity, 
# replace the file version with yours
# if the integrity is good, the output message will
# contain ... Good signature from  ...
gpg --verify gnupg-2.2.17.tar.bz2.sig # your version number may be different
```


For further information refer to
[GnuPG Integrity Check](https://gnupg.org/download/integrity\_check.html) and [Verify a PGP signature with GnuPG](https://www.circuidipity.com/verify-pgp-signature-gnupg/).


##### 2.2 Confidentiality assurance (20%)
GnuPG can be used to _secure communications_. Find a classmate works as your communication partner to complete the subtasks:
	
* Step 1: Use GnuPG, create a personal OpenPGP key pair.

```bash
# 1. Generate a personal GnuPG private key 
gpg --gen-key 

# follow the prompts, other than default settings
# provide you email and  secure passphrase

# 2. Export your private GnuPG key
# type the command in a single line
gpg --export-secret-keys -a "your email@pnw.edu" | tee "your name.pri"
# your private key is printed in the terminal
# and saved in the file "your name.pri" as well.

# 3. Export your public GnuPG key
gpg --export -a  "your email@pnw.edu" | tee "your name.pub"

# your public key is printed in the terminal
# and saved in the file "your name.pub" as well.
```
	
* Step 2: Publish(Upload) your OpenPGP public key to one of [OpenPGPkeyserver](http://keys.gnupg.net/),  [MIT PGP Public Key Server](https://pgp.mit.edu/), [Hockeypuck OpenPGP keyserver](http://keyserver.ubuntu.com/) and [Mailvelope Key Server](https://keys.mailvelope.com/), then tell your partner which server has your public key. _Some key servers may be blocked by the campus network, keep trying until you find a working one._

		
* Step 3: Watch this video [Encrypt Your Gmail/Yahoo/Outlook/iCloud and Other Webmail](https://youtu.be/\-Hz40\_P6bVE), using [Mailvelope](https://www.mailvelope.com/) to import your partner's public PGP key that published on a keyserver, send an encrypted and signed email to your partner, then decrypt and verify his/her encrypted and signed email that sent to you. Do you need to certify your partner's public key? _Work this task on your host machine_
 
```bash
# 1. Download the latest Firefox then unzip it
# Your version number may be different
# If it does not work on your virtual machine, then do this subtask on your host machine.
tar -jxf firefox-71.0.tar.bz2
# 2. Run it
cd firefox/ && ./firefox

# 3.Google 'Mailvelope firefox plugin', find it and install it
# 4.Configure Mailvelope
# 5. Import your key pairs and your friends public keys
# 6. Enjoy confidential correspondence
```


##### 2.3 Privacy assurance (30%)
GnuPG can be used to _protect data_. Create a folder 'test' containing at least three image files, use your OpenPGP key pair and your friend's public key (download from the GPG keyserver on which your friend published her/his public key) to complete the subtasks:
	
* Step 1: Check sum, encryption and decryption work on single file, for folder, folder needs to be compressed first.
	
```bash
# 1. Compress the folder test into test.bz2
tar -jcf test.bz2 test
```

* Step 2: Create then verify checksums of 'test.bz2'.
```bash
# 1. find the SHA256 checksum of test.bz2
sha256sum test.bz2 > test.bz2.sha256

# 2. verify the SHA256 checksum of test.bz2
sha256sum -c test.bz2.sha256
```

* Step 3: Import your friends' public keys. Download your friends' public key from the key servers they told you

```bash
# 1. Go to the folder holds your friends public keys
# import these public keys
gpg --import "your friend name.pub"

# list all keys, highlight your friend
gpg --list-key
# a key is identified by its ID, for example
# pub   2048R/1ED9DEF3 2019-12-12 [expires: 2021-12-11]
# uid          Good guy (for class demo) <good@pnw.edu>
# sub   2048R/76818986 2019-12-12 [expires: 2021-12-11]
# 
# pub means public key info, its ID=1ED9DEF3
# uid means user id, used in 
# encryption/decryption/signature/verification
# sub means private key info, its ID=76818986
```


* Step 4: Encrypt then decrypt 'test.bz2'
```bash
# 1. For personal credential storage
# to specify which key, use its ID
# 1.1 encrypt, the encrypted named as test.bz2.gpg by default
gpg -e -u 'your email@pnw.edu' -r 'your email@pnw.edu' test.bz2

# view the encrypted file
ls -l test.bz2*

# 1.2 decrypt, name the decrypted file as test.bz2.dec
# you need to supply your protection passphrase
gpg -d test.bz2.gpg -o test.bz2.dec

# compare the decrypted file with the original file
# no difference
diff test.bz2 test.bz2.dec

# 2. For confidential communication
# 2.1 encrypt a file for your partner with her public key
# her public key is implied by partner email@pnw.edu
# type the command in a single line
gpg -e -u 'your email@pnw.edu' -r 'partner email@pnw.edu' -o 'yourname to partner name.gpg'  test.bz2

# 2.2 email 'yourname to partner name.gpg' to your partner
# meanwhile, you received 'partner name to your name.gpg' 
# from your partner
# decrypt 'partner name to your name.gpg' 
# with your private key, type the command in one line
gpg -o 'partner name to your name' -d 'partner name to your name.gpg'

# extract the archive to see the images sent 
# from your partner
tar -jxf 'partner name to your name' -C 'partner-images'
# inside folder 'partner-images', check the images
```

	
* Step 5: Sign then verify 'test.bz2'
```bash
# 1. choose a jpeg image file, name it as 'your name.jpg'
# sign it with your private key
gpg -u 'your email@pnw.edu' -b 'your name.jpg'
# the signature is your name.jpg.sig

# 2.email both 'your name.jpg' and 'your name.jpg.sig' to your partner
# meanwhile, you received
# 'partner name.jpg' and 'partner name.jpg.sig'

# 3. verify signature with your partner's public key
gpg --verify 'partner name.jpg.sig' 
# the output should contain
# ... good signature from your partner...
```

	
* Step 6: Sign and encrypt, then Decrypt and verify 'test'
```bash
# 1. choose a jpeg image file, name it as 'your name2.jpg'
# encrypt with your partner's public key,
# then sign it with your private key
# type the command in one line
gpg -u 'your email@pnw.edu' -r 'partner email@pnw.edu'  -s --encrypt 'your name2.jpg'
# an encrypted and signed image is generated
# default name as 'your name2.jpg.gpg'

# 2.email  only 'your name2.jpg.gpg' to your partner
# since it contains both the encrypted image and signature
# meanwhile, you received 'partner name2.jpg.sig'

# 3. decrypt with your public key
# verify signature with your partner's public key
gpg --decrypt -o 'partner name2.jpg' 'partner name2.jpg.gpg' 
# the output should contain
# ... good signature from your partner...
# and the image is decrypted, check the image
```

	
	
For further information refer to [Gnu Privacy Guard (GnuPG) Mini Howto](https://www.dewinter.com/gnupg_howto/english/GPGMiniHowto.html) and [How do I encrypt a file or folder in my home directory?](https://statistics.berkeley.edu/computing/encrypt)


### Report

Write a report about the process you complete the tasks in the description, key screen snapshots are needed as evidences.


### References* 
* [Pretty Good Privacy.](https://en.wikipedia.org/wiki/Pretty\_Good\_Privacy)
* [GNU Privacy Guard.](https://en.wikipedia.org/wiki/GNU\_Privacy\_Guard)
* [Gpg4win.](https://en.wikipedia.org/wiki/Gpg4win)
* [GnuPG.](https://www.gnupg.org/)
* [PGP Tutorial.](http://uncovering-cicada.wikia.com/wiki/PGP\_TUTORIAL)
* [PGP tutorial.](https://www.forte.net/devdocs/reference/pgp\_tutorial.htm)
* [Gpg4win.](https://www.gpg4win.org)
* [The Gpg4win Compendium.](https://files.gpg4win.org/doc/gpg4win-compendium-en.pdf)
* [CAcert.](http://www.cacert.org/)
* [CAcert Wiki.](https://en.wikipedia.org/wiki/CAcert.org)
* [CrypTool.](https://en.wikipedia.org/wiki/CrypTool)
* [CrypTool Portal.](https://www.cryptool.org)
* [OpenPGP.](https://www.openpgp.org/)
* [Seahorse.](https://wiki.gnome.org/Apps/Seahorse)
* [FlowCrypt.](https://flowcrypt.com/)
* [Mailvelope Wiki.](https://en.wikipedia.org/wiki/Mailvelope)
* [Mailvelope official website.](https://www.mailvelope.com)
* [Mailvelope source code.](https://github.com/mailvelope/)
* [git.](https://git-scm.com/)
* [TortoiseGit.](https://tortoisegit.org/)
* [Git for Windows with TortoiseGit and GitHub.](http://dancingmonkeysaccelerated.blogspot.com/2012/03/git-for-windows-with-tortoisegit-and.html)
* [Git official tutorial.](https://git-scm.com/docs/gittutorial)
* [An Intro to Git and GitHub for Beginners.](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
* [Hello World about Github.](https://guides.github.com/activities/hello-world/)
* [GitHub Learning Lab.](https://lab.github.com/)
* [Signing Git commits with GPG on Windows.](https://jamesmckay.net/2016/02/signing-git-commits-with-gpg-on-windows/)
* [ Using GPG in TortoiseGit.](https://blog.rathena.cn/post/use-gpg-in-tortoisegit/)
* [Key server ](https://en.wikipedia.org/wiki/Key\_server\_\(cryptographic\))
* [PGP Global Directory.](https://keyserver.pgp.com)
* [sks Key Servers.](https://sks\-keyservers.net/)
* [SKS OpenPGP Key server.](https://keyserver.ubuntu.com/)
* [PGP Public Key Server.](https://pgp.key\-server.io/)
* [Encrypt Your Gmail/Yahoo/Outlook/iCloud and Other Webmail.](https://www.youtube.com/watch?v=\-Hz40\_P6bVE)