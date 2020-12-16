import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

azure_connection_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")

'''
https://stackoverflow.com/questions/53906986/how-do-i-authenticate-a-user-against-an-azure-storage-blob-in-python
https://stackoverflow.com/questions/43071624/how-to-give-a-python-script-limited-access-to-azure-blob-container
'''
def upload_video_to_azure_blob():
    blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)
    container_name = "videoofloki"
    if blob_service_client.get_container_client(container_name):
        loki_video_path = os.path.join('./tmp', 'lokisleeping.mov')
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=loki_video_path)
        print('Uploading to Azure Storage as blob: \n\t' + loki_video_path)

        with open(loki_video_path, "rb") as data:
            blob_client.upload_blob(data)
    else:
        container_client = blob_service_client.create_container(container_name)



def list_of_loki_video():
    print('\n Listing loki videos...')
    blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)
    container_name = "videoofloki"
    container_client = blob_service_client.get_container_client(container_name)

    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print('\t' + blob.name)



upload_video_to_azure_blob()
list_of_loki_video()