#!/usr/bin/python3
from fabric.api import *
import os

env.hosts = ['<IP web-01>', '<IP web-02>']

def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if not os.path.exists(archive_path):
        return False
    
    try:
        # Upload archive to /tmp/
        put(archive_path, "/tmp/")
        
        # Uncompress the archive to /data/web_static/releases/
        file_name = archive_path.split("/")[-1]
        folder_name = file_name.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}".format(folder_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(file_name, folder_name))
        
        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_name))
        
        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")
        
        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format(folder_name))
        
        return True
    except:
        return False
