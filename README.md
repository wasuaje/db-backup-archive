== Readme ==

* Clone the repo
* Create a virtual env
  ```
  python3 -m venv venv
  ```
* Install requirements
  ```
  pip install -r requirements.txt
  ```
* You'll need the Azure storage account conn string
  ```
  export AZURE_STORAGE_CONNECTION_STRING="<yourconnectionstring>"
  ```
* run the process
  ```
  python archive.py
  ```