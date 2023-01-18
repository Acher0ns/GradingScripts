# preset consists of output file suffix, clone time, prefix name, csv file or default
class ClonePreset:
    __slots__ = ['folder_suffix', 'clone_time', 'name', 'csv_path', 'append_timestamp']

    def __init__(self, name, folder_suffix, clone_time, csv_path, append_timestamp):
        self.name = name
        self.folder_suffix = folder_suffix
        self.clone_time = clone_time
        self.csv_path = csv_path
        self.append_timestamp = append_timestamp

    def __repr__(self) -> str:
        return f'ClonePreset(folder_suffix: {self.folder_suffix}, clone_time: {self.clone_time}, name: {self.name}, csv_path: {self.csv_path}, append_timestamp: {self.append_timestamp})'

    def __eq__(self, other) -> bool:
        if type(other) != ClonePreset:
            return False

        return repr(self) == repr(other)
