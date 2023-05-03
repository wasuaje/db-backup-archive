import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.core.exceptions import ResourceExistsError
import glob

containers = ["todocasero", "luma02", "luma01", "bosquejo"]

# environment variable into account.
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connect_str)


# try Create the container
for container in containers:
    try:
        container_name = f"backup-prod-{container}"
        container_client = blob_service_client.create_container(container_name)
    except ResourceExistsError:
        print("Container already exists...moving on!")
    finally:
        # Create a blob client using the local file name as the name for the blob
        filenames_list = glob.glob(f'{container}-backup*.sql')
        for file_name in filenames_list:
            blob_client = blob_service_client.get_blob_client(
                container=container_name, blob=file_name)
            try:
                # Upload the created file
                if not blob_client.exists():
                    print("\nUploading to Azure Storage as blob:\n\t" + file_name)
                    with open(file_name, "rb") as blob_bytes:
                        blob_client.upload_blob(blob_bytes)
            except Exception as ex:
                print("There was an error backing up files ...moving on! \n", ex)
