from .Google import Create_Service

from googleapiclient.http import MediaFileUpload #  para enviar arquivos
from googleapiclient.http import MediaIoBaseDownload  #  baixar

import os
import io


CLIENT_SECRET_FILE = 'google_drive\client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPE)

def download_images ():
    file_id = ['1-VBjUYmGp0rTvsyTJGRVTQ7846WUeD2X', '1ij_VXYBqCRoNCEVOcXaJMZ3p9kPkMQQc']
    file_name = ['sex_demanding_cat.jpg', 'bread_cat.jpg']
    
    for id, name in zip(file_id, file_name):
        request = service.files().get_media(fileId=id)
        
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=request)
        done = False
        
        while not done:
            status, done = downloader.next_chunk()
            print('Download Progress {0}'.format(status.progress()*100))
            
        fh.seek(0)
        #print(fh)
        with open(os.path.join('./Files', name), 'wb') as f:
            f.write(fh.read())
            f.close()
          
def uploade_data (user_email, folder_id, photo):

    file_name = [photo]
    mime_types = ['image/jpeg']
    
    for file in file_name:
    
        
        title = str(file).replace(" ","_").replace("(","").replace(")","").replace("#","").replace("'","").replace("\"","").replace("+","").replace("!","")
        
        file_metadata = {
            'name' : title,
            'parents' : [folder_id]
            
        }
        
        media = MediaFileUpload('{0}'.format('media/'+str(file_metadata['name'])), mimetype=mime_types[0])
        
        service.files().create(
            body = file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        print('imagem salva', file)

def get_file (name, folder_id):
    if folder_id == -1:

        list = service.files().list(q="mimeType = 'application/vnd.google-apps.folder'").execute() 
    else:
        query = f"parents = '{folder_id}'"
        list = service.files().list(q=query).execute() 
        #print(list)
        
    for file in list['files']:
            #print(file['name'],'searching for', name)
        
            if file['name'] == name:
                
                #print('file already exists')
                exist= True
                file_id = file['id']
                
                return file['name'], file['id']
            
    return  print('file not found')

def get_image (name, folder_id):
    
    query = f"parents = '{folder_id}'"
    list = service.files().list(q=query).execute()
    #print(name, '<<<<<<<<<<<<<<<<<')
    #print(list)
    #input('wait')
    for image in list['files']: 
        #print(image['name'],'>>>>>>>>>>>>>>')
        #print(name, image['name'], type(name), type(image['name']), len(str(name)), len(image['name']) )
        if image['name'] == str(name):
            #print(image)
            return  image['id']
    #input('wait')

def create_folder (folder_name = str(), user_email = None):
    
    print('criar arquivo no drive')

    if not user_email:
        return print('Não foi possivel identificar o usuario')
        
    else:
        list = service.files().list(q= "mimeType = 'application/vnd.google-apps.folder'").execute() 
        #print(list, len(list))
       # print(list['files'])
        
        exist = False
        file_id = str()
        
        for file in list['files']:
            #print(file)
        
            if file['name'] == user_email:
                
                #print('Folder {} already exists'.format(user_email))
                #id = file['id']
                exist= True
        
        if exist == False:
            
            folders =  [user_email]
        
            for folder in folders:
                file_data = {
                    'name': folder,
                    'mimeType' : 'application/vnd.google-apps.folder' 
                }

                service.files().create(body=file_data).execute()
        
        if get_file(user_email, -1):
            name, id = get_file(user_email, -1)
            
        query = f"parents = '{id}'"

        list = service.files().list(q=query).execute() 
        #print(list, '<<<<<<<<<<<<')
        for file in list['files']:
            print()
            if file['name'] == folder_name:
                
                #print('Folder {} already exists'.format(user_email))
                return  print('pasta {} ja existe e não sera criada novamente'.format(folder_name))
        
        folders = [folder_name]
        for folder in folders:
            file_data = {
                'name': folder,
                'mimeType' : 'application/vnd.google-apps.folder' ,
                'parents' : [id]
            }

            service.files().create(body=file_data).execute()
        
        ###  return folder id
        
        
        return print('pasta {} criada'.format(folder_name))

def get_folder_id (folder_name):
    
    list = service.files().list().execute() 
    #print(list, len(list))
    #print(list['files'])
    
    exist = False
    file_id = str()
    
    for file in list['files']:
        #print(file)
    
        if file['name'] == folder_name:
            
            #print('file {} exists'.format(folder_name))
            
            file_id = file['id']
            return file_id

def change_permission (id):
    
    request_body = {
        'role' : 'reader',
        'type' : 'anyone'
    }
    
    reponse = service.permissions().create(
        fileId=id,
        body=request_body
    ).execute()
    
    sharable_link = service.files().get(
        fileId=id,
        fields='webViewLink'
    ).execute()
    
    print(sharable_link)

#change_permission('1fcpThq9OPPido_Nc2wMWLlp5mFssQ9MA')

def list_files_in_folder (name):
    
    
    folder_id= '1ns_O3-F5_90edg1jQTd2Fb1ZTGcyj1xk'
    query = f"parents  = '{folder_id}'" 
    
    list = service.files().list(q=query).execute() 
    #list = service.files().list().execute() #ja retorna todas as pastas do drive
    files = list.get('files')
    
    nextPageToken = list.get('nextPageToken')
    
    while nextPageToken:
        
        list = service.files().list(q=query).execute() 
        files.extend(list.get('files'))
        nextPageToken = list.get('nextPageToken')
        
    print(files)

def delete_folder (owner_name, album_title):

    name, id = get_file(owner_name, -1)
    #get owner folder id

    
    name, id = get_file(album_title, id)
    
    delete = f"fileId : '{id}'"
    
    list = service.files().delete(fileId=id).execute()
    
def change_file_name (owner, file_name, new_name):
    
    
    name, id = get_file(owner, -1)
    print(id, '<<<<<<')
    name, id = get_file(file_name, id)
    
    body = {'name': new_name}
    
    change_file_name = service.files().update(fileId=id,
                                              body=body).execute()
    
    return print(f' >>>>>>>>>>> o nome da pasta >{file_name}< foi alterada para >{new_name} <<<<<<<<<<<<< ')