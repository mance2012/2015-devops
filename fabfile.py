from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.contrib.files import exists
from StringIO import StringIO
import sys

prod_host = '172.31.24.33'
user = 'ubuntu'

def environment():
    env.hosts = [prod_host]
    env.user = user

def deploy():
        if not exists('/var/www/html/2015-devops/'):
                run("git clone git@github.com:mance2012/2015-devops.git")
        else:
                run("cd /var/www/html/2015-devops/ && git pull origin master && php composer.phar install && php vendor/bin/phinx migrate -e production")
