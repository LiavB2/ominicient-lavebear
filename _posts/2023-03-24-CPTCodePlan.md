---
toc: true
layout: post
description: How I am going to contrubute to my groups final project feature.
categories: [Notes]
title: CPT Code Plan, Advanced Security Certbot, Cross-origing Security advancemnts
---

# Overview 

## Advanced Security Certbot
- Certbot is a popular tool used to automate the process of obtaining and renewing SSL/TLS certificates for websites.
    -  It works by communicating with the Let's Encrypt certificate authority, which provides free certificates for domain validation. 
    - Certbot verifies that the domain name is controlled by the user requesting the certificate and then generates and installs the certificate on the user's web server.
- Advanced security features of Certbot include the ability to configure HTTPS redirection and to automate the renewal of certificates before they expire. 
    - HTTPS redirection ensures that all traffic to the website is encrypted, preventing eavesdropping and tampering by third parties. 
    - Certificate renewal ensures that the website's security credentials remain up to date and valid, preventing browser warnings and other security issues.

## Cross-origing Security advancemnts
- Cross-origin security is a set of techniques used to prevent web pages from accessing resources on other domains without permission. 
    - This is done to prevent malicious websites from stealing data or performing unauthorized actions on behalf of the user. 
    - Cross-origin security advancements include the use of the SameSite cookie attribute to prevent cross-site request forgery (CSRF) attacks, as well as the implementation of content security policies (CSP) to prevent cross-site scripting (XSS) attacks.

## Example:
- Here is an example of how to configure HTTPS redirection using Certbot on an Apache web server:

```
    sudo apt-get update
    sudo apt-get install certbot python-certbot-apache
    sudo certbot --apache
```

- This will install Certbot and the Apache plugin, and then run the Certbot command to obtain and install the certificate and configure HTTPS redirection for the website.

## Another example
- Here is an example of how to set the SameSite cookie attribute in PHP:

```
    session_start();
session_set_cookie_params([
    'lifetime' => 86400,
    'path' => '/',
    'domain' => 'example.com',
    'secure' => true,
    'httponly' => true,
    'samesite' => 'Strict'
]);

```

- This code sets the SameSite cookie attribute to 'Strict', which means that the cookie will only be sent to the website's own domain and not to any other domains.

