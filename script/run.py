from data_type.command_object import Rsync
from data_type.host_object import LocalDispatcher
from data_type.host_object import LocalReceiver
from local.secret import machine_dispatch_01
from local.secret import machine_receive_01
from time import sleep
ld = LocalDispatcher(machine=machine_dispatch_01)
del machine_dispatch_01
lr_01 = LocalReceiver(machine=machine_receive_01)
del machine_receive_01
rs = Rsync(source=ld.source, destination=lr_01.destination)

while True:
    # if folder has content, execute command
    if ld.media_path_has_content():
        rs.sync()
    sleep(ld.wait_seconds)
