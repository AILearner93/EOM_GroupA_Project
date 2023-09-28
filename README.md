# 📁 File Sharing System

A Python-based file sharing system that uses sockets to allow users to send and download files from the server. Perfect for sharing files between computers in a local network.

## 🛠️ Installation

### Prerequisites
- Python 3.x
- pip

### Steps
1. Clone the repository:
```sh
   git clone https://github.com/dhodakiaN/EOM_GroupA_Project.git
```
2. Navigate to the project directory:
```sh
    cd EOM_GroupA_Project
```
3. Install Virtual Environment:
```sh
    pip install virtualenv
```
4. Create Virtual Environment:
```sh
    virtualenv env
```
5. Run Virtual Environment:
```sh
    env\Scripts\activate # source env/bin/activate
```
6. Install the required packages:
```sh
    pip install -r requirements.txt
```

## 🚀 Usage

   If MacOS or Linux

   1a. Create a `.env` file:
   ```sh
       touch .env
   ```
   or 
   If Windows OS

   1b. Create a `.env` file:
   ```sh
   New-Item .env -type file
   ```

2. Add the following environment variables to the `.env` file:
```js
    HOST=localhost
    PORT=9999
```

### 🖥️ Server
- Run The Server:
```sh
    python server/app.py
```
### 🖱️ Client
- Run The Client:
```sh
    python client/app.py
```

## 📚 Features
- [x] Upload files to the server
- [x] Download files from the server
- [ ] Encrypt files before  uploading
- [ ] Decrypt files after downloading
- [x] Authentication
