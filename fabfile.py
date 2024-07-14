#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers

execute: fab deploy -i ~/.ssh/id_rsa
"""

from fabric import task
from fabric.connection import Connection
from invoke import run as local
from datetime import datetime
from os.path import exists, isdir

env_hosts = ['100.26.246.105', '100.25.2.220']

@task
def do_pack(c):
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print(e)
        return None

@task
def do_deploy(c, archive_path):
    """distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        
        c.put(archive_path, '/tmp/')
        c.run('mkdir -p {}{}/'.format(path, no_ext))
        c.run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        c.run('rm /tmp/{}'.format(file_n))
        c.run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        c.run('rm -rf {}{}/web_static'.format(path, no_ext))
        c.run('rm -rf /data/web_static/current')
        c.run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as e:
        print(e)
        return False

@task
def deploy(c):
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack(c)
    if archive_path is None:
        return False
    for host in env_hosts:
        conn = Connection(host=host, user='ubuntu', connect_kwargs={"key_filename": "id_rsa"})
        if not do_deploy(conn, archive_path):
            return False
    return True