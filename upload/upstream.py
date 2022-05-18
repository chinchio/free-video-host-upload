from host.upstream_api import UpstreamApi

import json

class Upstream():
    def __init__(self, key: str, root_folder_id: int) -> None:
        self.upstream_api = UpstreamApi(key = key)
        self.root_folder_id = root_folder_id

    def remote_upload(self, url: str) -> str:
        upload_response =  self.upstream_api.upload_by_url(url= url, fld_id = self.root_folder_id)
        filecode = upload_response["result"]["filecode"]
        url = f'https://upstream.to/{filecode}'
        return url