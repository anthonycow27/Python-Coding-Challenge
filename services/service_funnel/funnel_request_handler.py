"""
Module determining type of request given by user
"""


class FunnelRequestHandler:

    def __init__(self, **kwargs):
        self.request = kwargs.get('request')
        self.snippet_dict = kwargs.get('snippet_dict')

    def get_request_type(self):
        if self.__is_first_type():
            return 0
        elif self.__is_second_type():
            return 1
        elif self.__is_third_type():
            return 2
        else:
            return None

    def __is_first_type(self):
        selected_tag_string = self.__get_name_string()
        if selected_tag_string in self.snippet_dict.keys():
            return True
        return False

    def __is_second_type(self):
        selected_tag_string = self.__get_name_string()
        for key in self.snippet_dict.keys():
            if selected_tag_string in key:
                return True
        return False

    def __is_third_type(self):
        selected_tag_string = self.__get_name_string()
        if selected_tag_string not in self.snippet_dict.keys():
            return True
        return False

    def __get_name_string(self):
        name_array = []
        for tag in self.request.get('selected_tags'):
            name_array.append(tag.get('name'))
        selected_tag_string = ','.join(sorted(name_array))
        return selected_tag_string
