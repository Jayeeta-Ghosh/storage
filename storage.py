import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = ''
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer')
    file_to = input('Enter the full path to upload the file in drop box') 

    # API v2
    transferData.upload_file(file_from, file_to)
    print('file has been moved')

if __name__ == '__main__':
    main()