# Finding Waldo

Welcome to the Finding Waldo challenge! Your task is to decrypt an encrypted message to find Waldo's location.

## Hints
1. The encryption algorithm used is AES.
2. The key used for encryption is 16 characters long and is a common phrase.
3. localhost:8000 is the server that has the encrypted message and the key with decryption capabilities.


## Pre-requisites
- Docker
## Deployment
To run the challenge, use the following commands:
```bash
cd '.\Finding Waldo\service\'  
```

```bash
docker-compose up --build
```

### Starting the challenge
- The challenge is available at `localhost:8000`
