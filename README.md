# File Upload REST API Documentation

This documentation details the usage of the File Upload REST API, designed to upload files to a specified AWS S3 bucket. Built with Flask, this API manages file uploads, secure filename processing, and interactions with AWS S3.

# How It Works
## Step 1: Filling the .env File

first fill the related credentials in the relative path:
credentials\.env

- `AWS_ACCESS_KEY_ID`: get this from aws IAM/Users.
- `AWS_SECRET_ACCESS_KEY`: get this from aws IAM/Users.
- `AWS_S3_BUCKET_NAME`: name of the bucket you created at AWS-S3.



## Step 2: Running the Project

```sh
pip install -r Requirements.txt
```

```sh
python run.py
```

## API Endpoint

**POST /upload**

## Base URL

```
https://your.domain.address
```


## Endpoint Description

This endpoint is designed for uploading files to an AWS S3 bucket. It requires a file part in the request and optionally accepts a custom filename.

## Request Parameters

- `file`: File to be uploaded (required).
- `filename`: Custom filename for the file (optional).

## Responses

- `200 OK`: File successfully uploaded.
- `400 Bad Request`: Missing file part in the request or no file selected.
- `500 Internal Server Error`: Upload to AWS failed.

## Example Usage Of API 

### Python

```python
import requests

def upload_file_to_api(api_url, file_path, custom_filename=None):
    with open(file_path, 'rb') as file:
        filename = custom_filename if custom_filename else file.name
        files = {'file': (filename, file)}
        data = {'filename': filename}

        response = requests.post(api_url, files=files, data=data)
        return response

# Usage
api_url = 'https://your.domain.address/upload'
file_path = './photo.png'
custom_filename = 'xxxxxx.png'

response = upload_file_to_api(api_url, file_path, custom_filename)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
```

### Javascript
```javascript
const fs = require('fs');
const axios = require('axios');
const FormData = require('form-data');

async function uploadFileToApi(apiUrl, filePath, customFilename = null) {
    const form = new FormData();
    const filename = customFilename || filePath.split('/').pop();
    form.append('file', fs.createReadStream(filePath), filename);
    form.append('filename', filename);

    try {
        const response = await axios.post(apiUrl, form, {
            headers: {
                ...form.getHeaders()
            }
        });
        return response.data;
    } catch (error) {
        return error.response.data;
    }
}

// Usage
const apiUrl = 'https://your.domain.address/upload';
const filePath = './photo.png';
const customFilename = 'xxxxxx.png';

uploadFileToApi(apiUrl, filePath, customFilename)
    .then(data => console.log(data))
    .catch(err => console.error(err));

```