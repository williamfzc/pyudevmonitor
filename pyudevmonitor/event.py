import typing
import json
from loguru import logger


class UEvent(object):
    """ convert udev info (str) into object """

    def __init__(self, udev_info_list: typing.List[str]):
        # args
        self.ACTION: str = ""
        self.DEVPATH: str = ""
        self.DEVTYPE: str = ""
        self.DRIVER: str = ""
        self.ID_BUS: str = ""
        self.ID_FOR_SEAT: str = ""
        self.ID_MODEL: str = ""
        self.ID_MODEL_ID: str = ""
        self.ID_PATH: str = ""
        self.ID_PATH_TAG: str = ""
        self.ID_REVISION: str = ""
        self.ID_SERIAL: str = ""
        self.ID_SERIAL_SHORT: str = ""
        self.ID_USB_INTERFACES: str = ""
        self.ID_VENDOR: str = ""
        self.ID_VENDOR_ENC: str = ""
        self.ID_VENDOR_FROM_DATABASE: str = ""
        self.ID_VENDOR_ID: str = ""
        self.INTERFACE: str = ""
        self.MAJOR: str = ""
        self.MINOR: str = ""
        self.MODALIAS: str = ""
        self.PRODUCT: str = ""
        self.SEQNUM: str = ""
        self.SUBSYSTEM: str = ""
        self.TAGS: str = ""
        self.TYPE: str = ""
        self.USEC_INITIALIZED: str = ""
        self.adb_user: str = ""

        # empty event
        self._empty: bool = False
        if not udev_info_list:
            logger.warning("empty udev event")
            self._empty: bool = True
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

    def is_empty(self) -> bool:
        return self._empty
