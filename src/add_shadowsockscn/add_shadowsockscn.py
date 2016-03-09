# -*- coding: utf-8 -*-

import argparse, getpass, sys
from .Domain import Domain
from .AutoBBS import AutoBBS

class shadowsockscn:
    def __init__(self,SS):
        self
    def parse_args(self):
        """
        Parse the arguments/options passed to the program on the command line.
        """
        parser = argparse.ArgumentParser(prog='CronWorker',
                                         description='Get free accounts from internet',
                                         epilog='For further use information,'
                                         'see the file README.md',)
        # positional
        parser.add_argument('-a',
                            '--auto_checkin',
                            dest='auto_checkin',
                            action='store_true',
                            default=False,
                            help='auto check in to get free 200-300MB')
        parser.add_argument('-u',
                            '--username',
                            action='store',
                            help='your shadowsocks username (email)')

        parser.add_argument('-p',
                            '--password',
                            action='store',
                            help='your shadowsocks password, '
                            'beware: it might be visible to other users on your system')
        args = parser.parse_args()
        return args
    def get(self):
        domain = Domain(hostname = 'www.shadowsockscn.com/')
        args = self.parse_args()
        # Query password, if not alredy passed by command line.
        if not args.username:
            args.username = input("Email: ")
        if not args.password:
            args.password = getpass.getpass(stream=sys.stderr)
        #print(args.username,args.password)
        if not args.username or not args.password:
            logging.error("You must supply username and password to log-in")
            exit(ExitCode.MISSING_CREDENTIALS)

        userName = args.username
        passWord = args.password
        autobbs = AutoBBS(domain = domain, userName=userName, passWord=passWord)
        st = autobbs.login()
        if st[1] and args.auto_checkin:
            autobbs.checkin()
        elif st[1]:
            aa = input("Ready to ckeck in, Y(es) or N(o): ")
            if(aa=="Y"or aa=="y" or aa=="yes"or aa=="Yes"):
                autobbs.checkin()
            else:
                print("Not going to checkin")
        servers = autobbs.getAccount()
        return servers
