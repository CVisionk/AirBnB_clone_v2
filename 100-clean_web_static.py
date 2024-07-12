#!/usr/bin/python3
from fabric.api import *
import os


env.hosts = ['<IP web-01>', '<IP web-02>']


def do_clean(number=0):
    """Deletes out-of-date archives."""
    number = int(number)
    if number == 0:
        number = 1

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
