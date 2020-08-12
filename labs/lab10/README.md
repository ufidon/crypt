# its350
course materials and references for its350

## Lab10: FIDO --- Fast IDentity Online

### Description
**FIDO** is the world’s largest ecosystem for standards-based, interoperable *multi-factor authentication*. It has two specifications: 
* the Universal Second Factor **U2F** protocol
* the Universal Authentication Framework **UAF** protocol

In this lab, you will learn and practice 

* what is FIDO? 
* How FIDO works? 
* How to use FIDO?
* How to deploy FIDO?

Lab requirements:

* a SEED virtual machine, i.e. Ubuntu 16.04
* an iOS or Android smartphone

	
### Task 1 (10%)
Read the following two articles and write a summary:

* [How FIDO Works](https://fidoalliance.org/how-fido-works/)
* [U2F & UAF Tutorial](./papers/FIDO-U2F-UAF-Tutorial-v1.pdf)

### Task 2 (30%)
DUO can not only be used for your PNW account, but also for many third-party accounts such as Gmail, Amazon, Facebook and DropBox, etc. that support FIDO.

Refer to the [online tutorial](https://guide.duo.com/third-party-accounts) to setup [DUO authentication](https://guide.duo.com/android) for your DropBox account(create one if you don't have).


### Task 3 (30%)
DUO is just one of many authenticators supporting FIDO. There are lots FIDO-compliant authenticators such as [Google authenticator](https://en.wikipedia.org/wiki/Google\_Authenticator), [Microsoft authenticator](https://docs.microsoft.com/en-us/azure/active-directory/user-help/user-help-auth-app-overview), etc.

Refer to the online tutorial [How to Set Up 2-Factor Authentication for Login and sudo](https://www.linux.com/topic/desktop/how-set-2-factor-authentication-login-and-sudo/) or [Install & Configure Google Authenticator in Ubuntu 16.04 & 17.04](https://thelinuxcode.com/install-configure-google-authenticator-ubuntu-16-04-17-04/) to 

1. setup Google authenticator for your SEED virtual machine. Use command 

```bash
# to open/modify/save the configuration file '/etc/pam.d/common-auth'.
sudo subl /etc/pam.d/common-auth
```

2. logout then login your virtual machine, it will ask for the password and a authentication code.

3.  *use \# to comment out the line 'auth required pam\_google\_authenticator.so' you added above to disable Google 2FA.*

### Task 4 (30%)
There are many open-source two-factor authentication applications for systems utilizing one-time password protocols --- HOTP and TOTP, such as [WinAuth](https://winauth.github.io/winauth), [Authenticator](https://gitlab.gnome.org/World/Authenticator),  [andOTP](https://github.com/andOTP/andOTP), [FreeOTP](https://freeotp.github.io/). This means that no proprietary server-side component is necessary: use any server-side component that implements these standards. There are open-source 2FA server as well: [LinOTP](https://www.linotp.org), [FreeIPA](https://www.freeipa.org/),  [privacyIDEA](https://github.com/privacyidea/privacyidea), [dynalogin](https://dynalogin.org).


* Use *FreeOTP* to setup 2FA for one of your Gmail accounts.


### Report

Write a report about the process you complete the tasks in the description, key screen snapshots are needed as evidences.


### References
* [Authenticator](https://en.wikipedia.org/wiki/Authenticator)
* [How to Use Google Authenticator on a Windows PC](https://www.maketecheasier.com/google-authenticator-windows/)
