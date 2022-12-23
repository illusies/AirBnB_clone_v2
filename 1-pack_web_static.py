#!/usr/bin/python3
'''
A Fabric script that generates a .tgz archive from the contents of the 
web_static folder of your AirBnB Clone repo, using the function do_pack
'''

from fabric.api import local
from datetime import datetime

from fabric.decorators import runs_once

@runs_once
def do_pack():
    '''A function that generates a .tgz archive'''
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(path))

    if result.failed:
        return None
    return path
