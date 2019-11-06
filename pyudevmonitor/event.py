import typing
import json


class UEvent(object):
    """ convert udev info (str) into object """

    def __init__(self, udev_info_list: typing.List[str]):
        for each_arg in udev_info_list[1:]:
            name, value = each_arg.split("=")
            self.__dict__[name] = value

    @property
    def desc(self) -> str:
        return json.dumps(self.__dict__)
