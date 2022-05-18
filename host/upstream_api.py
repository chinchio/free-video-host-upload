import requests
import json
from urllib.parse import urlencode

class UpstreamApi():
    """
    UpstreamApi
    reference: https://upstream.to/api.html
    """
    def __init__(self, key: str) -> None:
        self.base_url = "https://upstream.to"
        self.key = key
        pass

    def account_info(self) -> json:
        req_url = "{base_url}/api/account/info?key={key}"
        r = requests.get(req_url.format(base_url = self.base_url, key= self.key))
        return r.json()

    def account_status(self) -> json:
        req_url = "{base_url}/api/account/stats?key={key}"
        r = requests.get(req_url.format(base_url = self.base_url, key= self.key))
        return r.json()
    
    # didn't implement get upload server

    # didn't implement upload file to server

    def upload_by_url(self, url: str, fld_id: int = 0, cat_id: int = 0, file_public: bool = False, file_adult: bool = False, tags: str = "") -> json:
        selection_query_dict = {
            "fld_id": fld_id,
            "cat_id": cat_id,
            "file_public": file_public,
            "file_adult": file_adult,
            "tags": tags
        }
        req_url = "{base_url}/api/upload/url?key={key}&url={url}&" + urlencode(selection_query_dict)
        r = requests.get(req_url.format(base_url = self.base_url, key= self.key, url = url))
        return r.json()
    
    def file_info(self, file_code: str) -> json:
        req_url = "{base_url}/api/file/info?key={key}&file_code={file_code}"
        r = requests.get(req_url.format(base_url = self.base_url, key= self.key, file_code = file_code))
        return r.json()

    def file_edit(self, file_code: str, file_title: str) -> json:
        req_url = "{base_url}/api/file/edit?key={key}&file_code={file_code}&file_title={file_title}"
        r = requests.get(req_url.format(base_url = self.base_url, key= self.key, file_code = file_code, file_title = file_title))
        return r.json()

    def file_list(self) -> json:
        req_url = "{base_url}/api/file/list?key={key}"
        r = requests.get(req_url.format(base_url = self.base_url, key= self.key))
        return r.json()

    def file_clone(self, file_code: str) -> json:
        req_url = "{base_url}/api/file/clone?key={key}&file_code={file_code}"
        r = requests.get(req_url.format(base_url = self.base_url, key= self.key, file_code = file_code))
        return r.json()
    
    def delete_file(self, last: int) -> json:
        """
        Get last deleted files list
        last(int): Show files deleted in last X hours (e.g. 24)
        """
        req_url = "{base_url}/api/file/deleted?key={key}&last={last}"
        r = requests.get(req_url.format(base_url = self.base_url, key= self.key, last = last))
        return r.json()
    
    def folder_list(self, fld_id: int, files: int) -> json:
        """
        fld_id(int): Parent folder id, default=0(in api)
        files(int): Show file list in this folder
        """
        req_url = "{base_url}/api/folder/list?key={key}&fld_id={fld_id}&files={files}"
        r = requests.get(req_url.format(base_url = self.base_url, key= self.key, fld_id = fld_id, files = files))
        return r.json()

    def folder_create(self, name: str, parent_id: int) -> json:
        req_url = "{base_url}/api/folder/create?key={key}&name={name}&parent_id={parent_id}"
        r = requests.get(req_url.format(base_url = self.base_url, key= self.key, name = name, parent_id = parent_id))
        return r.json()

    # didn't implement folder edit

    # didn't implement file encodings