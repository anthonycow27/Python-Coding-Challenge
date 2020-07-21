"""
Module determine response rendering based on request type
"""
import json


class FunnelResponseHandler:

    def __init__(self, **kwargs):
        self.request_type = kwargs.get('request_type')
        self.snippet_dict = kwargs.get('snippet_dict')
        self.request = kwargs.get('request')

    def get_response(self):
        if self.request_type == 0:
            return self.__get_type_one_response()
        elif self.request_type == 1:
            return self.__get_type_two_response()
        elif self.request_type == 2:
            return self.__get_type_three_response()
        else:
            return {'error': 500}

    def __get_type_one_response(self):
        response = {}
        tag_string = self.__get_name_string()
        response.update({"snippet": json.dumps(
            str(self.snippet_dict.get(tag_string)))})
        response.update({"next_tags": []})
        response.update({"selected_tags": self.request.get('selected_tags')})
        response.update(
            {"status": {"code": 0, "msg": "Valid tags with snippet"}})
        return response

    def __get_type_two_response(self):
        response = {}
        tag_string = self.__get_name_string()
        response.update({"snippet": None})
        response.update({"next_tags": self.__get_next_tag(tag_string)})
        response.update({"selected_tags": self.request.get('selected_tags')})
        response.update(
            {"status": {"code": 1, "msg": "Valid tags but no snippet"}})
        return response

    def __get_type_three_response(self):
        response = {}
        response.update({"snippet": None})
        response.update({"next_tags": []})
        response.update({"selected_tags": self.request.get('selected_tags')})
        response.update({"status": {"code": 2, "msg": "Invalid tags"}})
        return response

    def __get_name_string(self):
        name_array = []
        for tag in self.request.get('selected_tags'):
            name_array.append(tag.get('name'))
        selected_tag_string = ','.join(sorted(name_array))
        return selected_tag_string

    def __get_next_tag(self, tag_string):
        next_tag_array = []
        name_array = self.__get_result_name_array(tag_string)
        for name in name_array:
            next_tag_array.append({'name': name})
        return next_tag_array

    def __get_result_name_array(self, tag_string):
        tag_array = []
        key_set = set()
        tag_set = set(tag_string.split(','))
        for key in self.snippet_dict.keys():
            if tag_string in key:
                key_copy = key.split(',')
                for key in key_copy:
                    if key not in tag_set:
                        key_set.add(key) 
        return list(key_set)
