from local.secret import machine_dispatch_01
from local.secret import machine_receive_01
from pathlib import Path


class LocalDispatcher:
    def __init__(self,
                 path_to_media:     Path,
                 clean_up=False,
                 wait_seconds=60):

        """
        :param path_to_media: Path, the directory-to-monitor for media-to-send
        :param clean_up: bool, whether or not to delete sent files
        :param wait_seconds: int, seconds to wait between dispatcher checks
        """
        self.path_to_media = path_to_media
        self.clean_up = clean_up
        self.wait_seconds = wait_seconds


class LocalReceiver:
    def __init__(self,
                 ip_address:    str,
                 password:      str,
                 user_name:     str):
        self.ip_address = ip_address
        self.password = password
        self.user_name = user_name
