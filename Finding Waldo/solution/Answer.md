# Table of Contents
- [Table of Contents](#table-of-contents)
- [Overview](#overview)
  - [Page overview](#page-overview)
  - [Steps to Solve the Challenge](#steps-to-solve-the-challenge)
    - [Example](#example)
      - [Form Submission](#form-submission)


# Overview

The challenge involves decrypting an encrypted message to find Waldo's location. The participants are provided with an encrypted message and need to use the correct decryption key to retrieve the original plaintext.

## Page overview
There are four pages in the challenge:
1. **Message Page**: This page displays the encrypted message in JSON format.
2. **Key Page**: This page displays the decryption key.
3. **Decryption Page**: This page contains a form to submit the decryption key and the encrypted message.
4. **Home Page**: This page contains a very friendly welcome page.

## Steps to Solve the Challenge

1. **Retrieve the Encrypted Message**
   - Visit `http://localhost:5000/message` to get the encrypted message in JSON format.
   - Example response:
     ```json
     {
         "encrypted_message": "G30tMv+ThtFNhuitft+HAt2IWJ/F+c/9BjyR72tfA8Xkhc+PLny6V7hEy30KYBLnXc/kG30fm/eAWrAGpDB7fQ=="
     }
     ```



2. **Decrypt the Message**
- Open your web browser and go to `http://localhost:5000/key`.
- Change the cookie value to true and refresh the page.
- The decryption key will be displayed on the page.


3. **Navigate to the Decryption Page**
   - Open your web browser and go to `http://localhost:5000/decrypt`.

4. **Submit the Form**
   - Click the "Decrypt" button to submit the form.
   - The decrypted message will be displayed if the decryption is successful.


### Example

- **Encrypted Message**: `G30tMv+ThtFNhuitft+HAj2FRg1sqtz7QtcaBzQNUHryhC2UCsFKE2LYfNpD8yiL`
- **Decryption Key**: `thisisaveryshhhh`

#### Form Submission

After submitting the form with the correct details, the decrypted message will be displayed as:

```
Decrypted Message: Waldo's location is CTF{42.3601,-71.0589}
```
