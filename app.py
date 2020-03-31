import os,sys,cmd,getpass
import src.menutext as m,src.authentication as a
from src.library import *
from src.database import sql


class MyShell(cmd.Cmd, object):
    intro = 'Welcome to the service shell.   Type help or ? to list commands.\n'
    prompt = '[Shell Prompt] :'

    # ----- basic commands -----
    def do_write(self, arg):
        'Write somethings 23 sd -f -se'
        print(parse(arg))
    
    def do_help(self, line):
        for item in m.get_help():
            print(item)
    
    def do_login(self,line):
        print(line)
        username = input('Please enter username: ')
        password = getpass.getpass(prompt='Please enter password: ')
        
        if a.login(username,password) == True:
            print('Welcome..!!!')
        else:
            print('The answer entered by you is incorrect..!!!')
        
    def do_logout(self, line):
        print(line)
        print('Good Bye..!!!')
    
    def do_start(self, line):
        print(line)
        print('Scheduler Service started')
        
    def do_restart(self, line):
        print(line)
        print('Schedular Service restarted')
    
    def do_stop(self, line):
        print('Schedular Service stopped')
        
    def do_reset_config(self, line):
        print(line)
        print('All System Config was reset')
    
    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '



    def do_clear(self,line):
        os.system('cls')  # on windows
        #os.system('clear')  # on linux / os x

    def do_exit(self, line):
        return True

    def do_EOF(self, line):
        return True
    
    def cmdloop(self, intro=None):
        print(self.intro)
        while True:
            try:
                super(MyShell, self).cmdloop(intro="")
                break
            except KeyboardInterrupt:
                print("^C")
    
    




def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(str, arg.split()))

if __name__ == '__main__':
    sql.start()
    app = MyShell()
    app.cmdloop()