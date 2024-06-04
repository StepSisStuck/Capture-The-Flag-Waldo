# Table of Contents
- [Table of Contents](#table-of-contents)
- [Overview](#overview)
  - [Page overview](#page-overview)
  - [Steps to Solve the Challenge](#steps-to-solve-the-challenge)
      - [Encryption and Decryption Details](#encryption-and-decryption-details)
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

#### Encryption and Decryption Details

- **Encryption**: The message is encrypted using AES in ECB mode with PKCS7 padding.
- **Decryption**:
  1. The encrypted message is base64-decoded.
  2. AES decryption is performed using the provided key.
  3. The decrypted message is unpadded using the PKCS7 padding scheme.
  4. The original plaintext message is displayed.

### Example

- **Encrypted Message**: `G30tMv+ThtFNhuitft+HAuS8kJaZTs3brXfv6a6dQY063vnONWRR6w59W7TjP9Ua`
- **Decryption Key**: `thisisaveryshhhh`

#### Form Submission

After submitting the form with the correct details, the decrypted message will be displayed as:

```
Decrypted Message: Waldo's location is 42.3601,-71.0589
```
