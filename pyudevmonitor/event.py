import typing
import json
from loguru import logger


class UEvent(object):
    """ convert udev info (str) into object """

    def __init__(self, udev_info_list: typing.List[str]):
        if not udev_info_list:
            logger.warning("empty udev event")
            return
        logger.info("udev event start")
        for each_arg in udev_info_list[1:]:
            logger.debug(each_arg)
            name, value = each_arg.split("=")
            self.__dict__[name] = value
        logger.info("udev event end")

    @property
    def desc(self) -> str:
        return json.dumps(self.__dict__)
