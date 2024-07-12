#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    local("mkdir -p versions")
    archive_name = "versions/web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    result = local("tar -cvzf {} web_static".format(archive_name))
    if result.failed:
        return None
    return archive_name