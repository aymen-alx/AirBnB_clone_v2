#!/usr/bin/python3
"""
     Compress before sending
"""

from fabric.api import *
import os
from os import path
from datetime import datetime


def do_pack():
    """
         Compress before sending
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        if path.exists("./versions") is False:
            local('mkdir versions')

        archive_name = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None
