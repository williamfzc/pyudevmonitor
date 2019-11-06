import subprocess
import time
import typing
from loguru import logger
import threading

from pyudevmonitor.event import UEvent


class UDevMonitor(object):
    """ udevadm process management """
    def __init__(self, monitor_args: typing.List[str] = None, encoding: str = None):
        self.monitor_args: typing.List[str] = monitor_args or ["-u", "--subsystem-match=usb", "--environment"]
        self.encoding: str = encoding or "utf-8"

        self._process: typing.Optional[subprocess.Popen] = None

    def start(self):
        self._process = subprocess.Popen(
            ["udevadm", "monitor", "-u", *self.monitor_args],
            stdout=subprocess.PIPE,
        )
        time.sleep(1)
        assert self.is_running(), "udevadm not running"
        logger.info("udevadm process up")

        # ignore unused header
        self.read_event(drop=True)

    def stop(self):
        if self._process and self.is_running():
            self._process.kill()
            self._process = None
            logger.info("udevadm process down")
        else:
            logger.warning("udevadm process already down without killing")

    def is_running(self) -> bool:
        return not bool(self._process.poll())

    def read_line(self) -> str:
        return self._process.stdout.readline().decode("utf-8")

    def read_event(self, drop: bool = None) -> typing.Optional[UEvent]:
        event_content = []
        new_line = self.read_line().strip()
        while new_line:
            event_content.append(new_line)
            new_line = self.read_line().strip()
        if drop:
            return None
        return UEvent(event_content)

    def loop_read(self, to: typing.List[UEvent]) -> typing.Callable:
        stop: bool = False

        def loop():
            while not stop:
                new = self.read_event()
                to.append(new)
            logger.info("loop read stopped")

        def stop_loop():
            nonlocal stop
            stop = True

        threading.Thread(target=loop).start()
        return stop_loop
