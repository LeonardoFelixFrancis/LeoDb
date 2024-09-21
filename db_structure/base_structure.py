class BaseStructure: 

    def get_file_name(self, name):
        return f'{self.__class__.__name__}_{name}.leodb'