from os import close
import sqlite3
from sqlite3.dbapi2 import Connection, Cursor

con = sqlite3.connect('./Console_DB/db.sqlite3') 
cur = con.cursor()
print('Enter your SQL commands')
print('Use "help" if you want to know the available commands')
print('Blank line if clear input command')
command_buff = ''
while True: 
    user_command = input('>>>')
    command_buff += user_command

    if command_buff.startswith('select') :
        if not user_command :
            command_buff = ''
        else : 
            try:
                for i in cur.execute(command_buff):
                    print(i)
            except sqlite3.OperationalError:
                print('Error! Repeat the input.')
            command_buff = ''    

    elif command_buff.startswith('help') :
        if not user_command :
            command_buff = ''
        else:
            print('Use to print all in Table: "select * from Bike"')
            print('Use to print all by filter in Table: "select * from Bike where <filter>" ')
            print('Use to add in Table: "insert into Bike values(\'color\',lenght,wheels_count);"')
            print('Use to save changes in Table: "commit"')
            print('Use to delete last string in Table: "delete"')

            print('Use to exit: "exit"')
            command_buff = ''

    elif command_buff.startswith('commit') :
        if not user_command :
            command_buff = ''
        else : 
            con.commit()
            print('Saved!')
            command_buff = ''

    elif command_buff.startswith("insert") :
        if not user_command :
            command_buff = ''
        else : 
            try:
                count = 0
                for i in cur.execute('select * from Bike'):
                        count +=1 
                ins = command_buff[:command_buff.find('(')+1]+str(count+1)+','+command_buff[command_buff.find("'"):]
                cur.execute(ins)
            except sqlite3.OperationalError:
                print('Error! Repeat the input.') 
            command_buff = ''

    elif command_buff.startswith("delete") :
        if not user_command :
            command_buff = ''
        else : 
            try:
                count = 0
                for i in cur.execute('select * from Bike'):
                        count +=1 
                cur.execute(command_buff + ' from Bike where id = ' + str(count) )
            except sqlite3.OperationalError:
                print('Error! Repeat the input.') 
            command_buff = ''

    elif command_buff.startswith('exit') : 
        break

    else:
        command_buff = ''
        

con.close()


