#!/usr/bin/env python
from os import system

if __name__ == "__main__":
    system('python3 createdb.py')
    system('oidc-register https://iddev.fedorainfracloud.org/ http://localhost:5005/oidc_callback')
    system('python3 runserver.py -c config')

