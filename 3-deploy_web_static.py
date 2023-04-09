#!/usr/bin/python3
"""
    Full deployment
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['54.209.86.160', ' 3.84.161.254']


def do_pack():
    """
        Compress before sending
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        if path.exists("./versions") is False:
            local('mkdir versions')
            # print('yes')

        archive_name = "versions/web_static_{}.tgz".format(date)
        print(archive_name)
        local("tar -czvf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Deploy archive!
    """
    if path.exists(archive_path) is False:
        return False
    try:
        archive_name = archive_path.split('/')[-1]
        file_name = archive_name.split('.')[0]
        des = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(des, file_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive_name, des, file_name))
        run('rm /tmp/{}'.format(archive_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(des, file_name))
        run('rm -rf {}{}/web_static'.format(des, file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(des, file_name))
        return True
    except Exception:
        return False


def deploy():
    """
    Full deployment
    """
    new_archive = do_pack()
    if new_archive is not None:
        return do_deploy(new_archive)
    return False
