from subprocess import run


class Rsync:
    def __init__(self,
                 dispatcher,
                 receiver):
        self.dispatcher = dispatcher
        self.receiver = receiver

    def build_command_with_(self, file) -> list:
        command = [
            "rsync",
            "-uvah",
            "--stats",
            "--progress",
            str(file),
            self.receiver.destination]
        return command

    def execute_command_with_(self, files):
        commands, outputs = list(), list()
        for file in files:
            command = self.build_command_with_(file)
            commands.append(command)
        for command in commands:
            output = run(
                args=command,
                capture_output=True)
            if not client_returns_daemonized_(output):
                print(f'rsync daemon is not setup on the receiver')
            outputs.append(output)
        return outputs

    def sync(self, files):
        if not files:
            return
        self.execute_command_with_(files)


def client_returns_daemonized_(output) -> bool:
    password_request = 'askpass'
    output = str(output)
    return False if password_request in output else True
