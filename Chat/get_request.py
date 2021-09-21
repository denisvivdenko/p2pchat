from typing import Tuple

class GET:

    
    def __init__(self, request: str = -1, address_to_send: Tuple[str, int] = (), file_name: str = ''):
        if isinstance(request, str):
            self.address_to_send: Tuple[str, int] = self.__parse_query_GET_address(request)
            self.file_name = self.__parse_query_GET_file(request)
        else:
            self.address_to_send = address_to_send
            self.file_name = file_name

    def get_query(self):
        return f'GET\n{self.address_to_send[0]}\n{self.address_to_send[1]}\n{self.file_name}'

    def __parse_query_GET_address(self, query: str):
        lines = query.split('\n')
        return lines[1].strip(), int(lines[2])

    def __parse_query_GET_file(self, query: str):
        lines = query.split('\n')
        return lines[-1]