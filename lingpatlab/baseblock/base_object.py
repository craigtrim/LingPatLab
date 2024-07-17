# -*- coding: utf-8 -*-


import logging
from hashlib import md5


# TODO: consider incorporating these comments - https://blog.guilatrova.dev/how-to-log-in-python-like-a-pro/
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(filename)s : %(funcName)s() : %(lineno)d : %(message)s',
    level=logging.DEBUG)


class BaseObject(object):

    def __init__(self,
                 component_name: str):
        """ Change Log

        Created:
            29-Sept-2021
            craigtrim@gmail.com
        Updated:
            31-Mar-2023
            craigtrim@gmail.com
            *   add hash function
                https://github.com/craigtrim/baseblock/issues/5#issuecomment-1492393613

        Args:
            component_name (str): the name of the component to log for
        """
        self.logger = logging.getLogger(component_name)
        isEnabledFor = self.logger.isEnabledFor
        self.isEnabledForDebug = isEnabledFor(logging.DEBUG)
        self.isEnabledForInfo = isEnabledFor(logging.INFO)
        self.isEnabledForWarning = isEnabledFor(logging.WARNING)

    def get_logger(self) -> logging.Logger:
        return self.logger

    def component_name(obj: object) -> str:
        return str(obj.__class__).split("<class '")[-1].split("'")[0]

    @staticmethod
    def uuid_generator() -> str:
        from uuid import uuid1
        return str(uuid1()).replace('-', '_')

    @staticmethod
    def md5hash(input: str) -> int:
        if type(input) != str:
            raise NotImplementedError(type(input))

        return int(md5(input.encode('utf-8')).hexdigest(), 16)
