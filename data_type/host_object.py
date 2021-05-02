from os import walk
from pathlib import Path


class LocalDispatcher:
    def __init__(self,
                 machine: dict,
                 clean_up=False,
                 wait_seconds=60):

        """
        :param machine: relevant details for the dispatching machine
        :param clean_up: bool, whether or not to delete sent files
        :param wait_seconds: int, seconds to wait between dispatcher checks
        """
        self.path_to_media = machine['path to media']
        self.clean_up = clean_up
        self.wait_seconds = wait_seconds
        self.source = self.build_source()

    def build_source(self) -> str:
        source = ''
        source = source + self.path_to_media
        return source

    def media_path_has_content(self) -> bool:
        found_files = list()
        for root, _, files in walk(self.path_to_media):
            for file in files:
                found_files.append(Path(root, file))
        return True if found_files else False


class LocalReceiver:
    def __init__(self,
                 machine: dict):
        # save
        self.ip_address = machine['ip address']
        self.password = machine['password']
        self.user_name = machine['user_name']
        self.path_to_receive = machine['path to receive']
        # build
        self.destination = self.build_destination()

    def build_destination(self) -> str:
        destination = ''
        destination = destination + self.user_name
        destination = destination + '@'
        destination = destination + self.ip_address
        destination = destination + ':'
        destination = destination + self.path_to_receive
        return destination
