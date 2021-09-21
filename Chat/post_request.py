class POST:


    def __init__(self, request: str = -1, file_name: str = '', data: str = ''):
        if isinstance(request, str):
            self.data = self.__parse_POST_data(request)
            self.file_name = self.__parse_POST_file_name(request)
        else:
            self.data = data
            self.file_name = file_name

    def get_query(self):
        return f'POST\n{self.file_name}\n{self.data}'

    def __parse_POST_data(self, query: str): #TODO
        lines = query.split('\n')
        data = '\n'.join(lines[2:])
        return data

    def __parse_POST_file_name(self, query: str): #TODO
        lines = query.split('\n')
        return lines[1]