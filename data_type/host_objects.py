from local.secret import
from pathlib import Path


class LocalDispatcher:
    def __init__(self,
                 clean_up:          bool,
                 path_to_media:     Path):
        """
        :param path_to_media: Path, the directory-to-monitor for media-to-send
        :param clean_up: bool, whether or not to delete sent files
        """
        self.path_to_media = path_to_media
        self.clean_up = clean_up


class LocalReceiver:
    def __init__(self,
                 ip_address:    str,
                 password:      str,
                 user_name:     str):
        self.ip_address = ip_address
        self.password = password
        self.user_name = user_name
