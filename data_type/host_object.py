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
        self.found_file_list = list()

    def build_source(self) -> str:
        source = ''
        source = source + self.path_to_media
        return source

    def found_files(self) -> list:
        del self.found_file_list
        found_files = list()
        for root, _, files in walk(self.path_to_media):
            for file in files:
                found_files.append(Path(root, file))
        self.found_file_list = found_files
        return found_files


class LocalReceiver:
    def __init__(self,
                 machine: dict):
        # save
        self.ip_address = machine['ip address']
        self.rsyncd_module = machine['rsyncd module']
        self.password = machine['password']
        self.user_name = machine['user_name']
        self.path_to_receive = machine['path to receive']
        # build
        self._destination = self.build_destination()
        self._rsyncd_module_destination = self.build_module_destination()

    def build_destination(self) -> str:
        destination = '' + self.user_name + '@' + self.ip_address + \
                      ':' + self.path_to_receive
        return destination

    def build_module_destination(self) -> str:
        destination = self.destination.split(':')[0] + '::' + self.rsyncd_module
        return destination

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        print(f'do not use this setter, setting \'{value}\' failed')

    @property
    def module_destination(self):
        return self._rsyncd_module_destination

    @module_destination.setter
    def module_destination(self, value):
        print(f'do not use this setter, setting \'{value}\' failed')
