import requests
import json

class StreamtapeApi():
    """
    reference: https://streamtape.com/api
    """
    def __init__(self, login: str, key: str) -> None:
        self.base_url = "https://api.streamtape.com"
        self.login = login
        self.key = key

    def account_infos(self) -> json:
        """
        Everything account related (total used storage, reward, ...)
        """
        req_url = "{base_url}/account/info?login={login}&key={key}"
        r = requests.get(req_url.format(base_url = self.base_url, login = self.login, key = self.key))
        return r.json()
    
    def download_ticket(self, file: str) -> json:
        """
        preparing a download
        """
        req_url = "{base_url}/file/dlticket?file={file}&login={login}&key={key}"
        r = requests.get(req_url.format(base_url = self.base_url, file = file, login = self.login, key = self.key))
        return r.json()
    
    def download_link(self, file: str, ticket) -> json:
        """
        get a download link by using download ticket
        """
        req_url = "{base_url}/file/dl?file={file}&ticket={ticket}"
        r = requests.get(req_url.format(base_url = self.base_url, file = file, ticket = ticket))
        return r.json()
    
    def file_info(self, file: str) -> json:
        """
        check the status of a file, e.g. if the file exists

        file(str): allow pass more than one file id, use comma separated
        e.g. wg8ad12d3QiJRXG,wg8ad12d3QiJRXG4,wg8ad12d3QiJRXG5
        """
        req_url = "{base_url}/file/info?file={file}&login={login}&key={key}"
        r = requests.get(req_url.format(base_url = self.base_url, file = file, login = self.login, key = self.key))
        return r.json()
    
    # didn't implement upload function

    def add_remote_upload(self, url: str, folder: str, headers: str, name: str) -> json:
        """
        Remote Uploading a file
        !!!WARNING!!!
        if `url` include symbol `&`, add remote upload will fail.
        """
        req_url = "{base_url}/remotedl/add?login={login}&key={key}&url={url}&folder={folder}&headers={headers}amp;name={name}"
        r = requests.post(
            req_url.format(
                base_url = self.base_url, 
                login = self.login,
                key = self.key,
                url = url,
                folder = folder,
                headers = headers,
                name = name
                )
            )
        return r.json()
    
    # didn't implement remove remote upload

    def check_remote_upload_status(self, id: str) -> json:
        """
        Check Status of Remote Upload
        id(str): remote upload id
        """
        req_url = "{base_url}/remotedl/status?login={login}&key={key}&id={id}"
        r = requests.get(req_url.format(base_url = self.base_url, login = self.login, key = self.key, id = id))
        return r.json()
    
    def list_folder_or_files(self, folder: str) -> json:
        """
        Shows the content of your folders
        """
        req_url = "{base_url}/file/listfolder?login={login}&key={key}&folder={folder}"
        r = requests.get(req_url.format(base_url = self.base_url, login = self.login, key = self.key, folder = folder))
        return r.json()

    def create_folder(self, name: str, pid: str) -> json:
        """
        Creates a new folder
        pid(str): parent folder id
        """
        req_url = "{base_url}/file/createfolder?login={login}&key={key}&name={name}&pid={parent}"
        r = requests.get(req_url.format(base_url = self.base_url, login = self.login, key = self.key, name = name, parent = pid))
        return r.json()

    def rename_folder(self, id: str, name: str) -> json:
        """
        Renames a Folder
        id(str): folder id
        name(str): new folder name
        """
        req_url = "{base_url}/file/renamefolder?login={login}&key={key}&folder={folder}&name={name}"
        r = requests.get(req_url.format(base_url = self.base_url, login = self.login, key = self.key, folder = id, name = name))
        return r.json()

    def delete_folder(self, id: str) -> json:
        """
        Delete Folder
        id(str): folder id
        """
        req_url = "{base_url}/file/deletefolder?login={login}&key={key}&folder={folder}"
        r = requests.get(req_url.format(base_url = self.base_url, login = self.login, key = self.key, folder = id))
        return r.json()
    
    def rename_file(self, id: str, name: str) -> json:
        """
        Renames a File
        id(str): file id
        name(str): new file name
        """
        req_url = "{base_url}/file/rename?login={login}&key={key}&file={file}&name={name}"
        r = requests.get(req_url.format(base_url = self.base_url, login = self.login, key = self.key, file = id, name = name))
        return r.json()
    
    def move_file(self, file_id: str, folder_id: str) -> json:
        """
        Move File
        """
        req_url = "{base_url}/file/move?login={login}&key={key}&file={file}&folder={folder}"
        r = requests.get(req_url.format(base_url = self.base_url, login = self.login, key = self.key, file = file_id, folder = folder_id))
        return r.json()
    
    def delete_file(self, id: str) -> json:
        """
        Delete File
        id(str): file id
        """
        req_url = "{base_url}/file/delete?login={login}&key={key}&file={file}"
        r = requests.get(req_url.format(base_url = self.base_url, login = self.login, key = self.key, file = id))
        return r.json()
    
    def list_runing_coverts(self) -> json:
        """
        Lists running converts
        """
        req_url = "{base_url}/file/runningconverts?login={login}&key={key}"
        r = requests.get(req_url.format(base_url = self.base_url, login = self.login, key = self.key))
        return r.json()

    def list_failed_coverts(self) -> json:
        """
        Lists failed converts
        """
        req_url = "{base_url}/file/failedconverts?login={login}&key={key}"
        r = requests.get(req_url.format(base_url = self.base_url, login = self.login, key = self.key))
        return r.json()

    def get_thumnail_image(self, id: str) -> json:
        """
        Get Thumnail image
        id(str): file id
        """
        req_url = "{base_url}/file/getsplash?login={login}&key={key}&file={file}"
        r = requests.get(req_url.format(base_url = self.base_url, login = self.login, key = self.key, file = id))
        return r.json()
