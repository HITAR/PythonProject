from xlwt import Workbook
import xlwt
import xgboost
book = Workbook()
sheet1 = book.add_sheet('Sheet 1')


file = open('E:\\data.txt','r')
row0 = ['rank','dt','cookie','ip','idfa','imei','android_id','openudid','mac','timestamps','camp_id',
        'creativeid:','mobile_os','mobile_type','app_key','app_name','placement_id','user_agent','media_id',
        'os','born_time','flag']
style0 = xlwt.easyxf()
for i in range(0,len(row0)):
    sheet1.write(0,i,row0[i],style0)
list = []
j = 1
for line in file.readlines():
    list = [x for x in line.strip('\n').split('\x01')]
    #print(list)
    if list[-1] == '1':
        print(list)
    for i in range(0,len(list)):
        sheet1.write(j,i,list[i],style0)
    j+=1

book.save('E:\\result.xls')
file.close()

