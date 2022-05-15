from host.streamtape_api import StreamtapeApi

import json
import logging
from datetime import date
import uuid
import time

class Streamtape():
    def __init__(self, api_username: str, api_password: str, root_folder_id: str) -> None:
        self.streamtape_api = StreamtapeApi(api_username, api_password)
        self.root_folder_id = root_folder_id
        self.datetime = date.today()
    
    # generate unique folder id (by date and uuid)
    def _get_upload_folder_id(self) -> str:
        uuid4_ = str(uuid.uuid4())
        day_folder_id = self._create_folder_layer_by_date()
        upload_folder_id = self._create_folder_if_not_exists(day_folder_id, uuid4_)["result"]["folderid"]
        return upload_folder_id

    def _create_folder_layer_by_date(self) -> str:
        """
        Crete folder layer by date
        (It's because streamtape remote upload didn't return file id.)
        (I need a easy and stupid way to find out the correct file id.)
        -------------------------------------
        {root_folder_id}/{year}/{month}/{day}
        return {day} folder id
        """
        last_folder_id = self.root_folder_id
        folders = [str(self.datetime.year), str(self.datetime.month), str(self.datetime.day)]
        for folder in folders:
            last_folder_id = self._create_folder_if_not_exists(last_folder_id, folder)
        
        return last_folder_id
        
    
    def _create_folder_if_not_exists(self, id: str, folder_name: str) -> str:
        """
        Create folder if not exists
        if this folder name exist in this folder layer then return their folder id, else create new folder and return new folder id.
        id(str): current layer folder id
        name(str): folder name
        """
        folders = self.streamtape_api.list_folder_or_files(id)["result"]["folders"]
        folder_exist: bool = False
        folder_id: str = ""

        for folder in folders:
            if folder_name == folder["name"]:
                folder_exist = True
                folder_id = folder["id"]
        if not folder_exist:
            folder_id = self.streamtape_api.create_folder(folder_name, id)
        
        return folder_id
    
    # main_call
    def remote_upload(self, remote_upload_url: str, headers: str, filename: str) -> json:
        folder_id: str = self._get_upload_folder_id()

        before_upload_response = self._ls_folder(folder_id)

        #upload
        self._add_remote_upload(remote_upload_url= remote_upload_url, folder_id= folder_id, headers= headers, filename= filename)

        while before_upload_response == self._ls_folder(folder_id):
            time.sleep(5)
        
        print(self._ls_folder(folder_id)["result"]["files"][0]["link"])
        


    def _add_remote_upload(self, remote_upload_url: str, folder_id: str, headers: str, filename: str) -> json:
        try:
            upload_response = self.streamtape_api.add_remote_upload(url= remote_upload_url, folder= folder_id, headers=headers, name= filename)
            #print(upload_response)
            self.file_id = upload_response["result"]["id"]
            self.folder_id = folder_id
            return upload_response
        except:
            logging.error("upload fail")
    
    def _ls_folder(self, id: str) -> json:
        try:
            get_link_response = self.streamtape_api.list_folder_or_files(id)
            #print(get_link_response)
            return get_link_response
        except:
            logging.error("get link fail")
