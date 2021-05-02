from subprocess import run


class Rsync:
    def __init__(self,
                 source,
                 destination):
        self.source = source
        self.destination = destination

    def build_command(self) -> list:
        command = [
            'rsync',
            '-uvah --stats --progress',
            self.source,
            self.destination]
        return command

    def execute(self):
        output = run(
            args=self.build_command(),
            capture_output=True)
        return output

    def sync(self):
        self.execute()
