import win32netcon
import traceback
import sys
import win32net
import sysconfig

def getall_users(server):
   '''This functions returns a list of id and full_names on an NT server'''
   j=1
   res=1
   users=[]
   user_list=[]
   try:
       while res:
          (users,total,res) = win32net.NetUserEnum(server,3,win32netcon.FILTER_NORMAL_ACCOUNT,res,win32netcon.MAX_PREFERRED_LENGTH)
          for i in users:
             add=0
             login=str(i['name'])
             info_dict=win32net.NetUserGetInfo(server, login, 3)
             full_name=str(info_dict['full_name'])
             j=j+1
             user_list.append(login+'\t'+full_name)
       return user_list
   except win32net.error:
       print(traceback.format_tb(sys.exc_info()[2]),'\n',sys.exc_type,'\n',sys.exc_value)

print(getall_users(r'\\anran-PC'))