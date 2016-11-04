from xlwt import Workbook
import xlwt
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

book = Workbook()
sheet1 = book.add_sheet('Sheet 1')

def SavetoExcel():
    file = open('D:\\BaiduYunDownload\\AdMaster_competition_dataset\\AdMaster_test_dataset\\final_ccf_test_0919','r')
    #file = open('E:\\data.txt')
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
        data = np.hstack(list)
        #data = np.array(list)
        # print(data)
        # if list[-1] == '1':
        #     print(list)
        for i in range(0,len(list)):
            sheet1.write(j,i,list[i],style0)
        j+=1
    print(data)
    book.save('E:\\result.csv')
    file.close()
    return data


def readcsv():
    le = LabelEncoder()
    print("start read CSV")
    destination = pd.read_csv(LABEL_FINAL_CSV, header=0, index_col=0)
    x_test = pd.read_csv(TEST_FINAL_CSV, header=0, index_col=0)
    print("Over read Csv")
    y = le.fit_transform(destination['country_destination'].values)
    idSave = x_test.index


if __name__ == "__main__":

    # lbl_enc = LabelEncoder()
    # lbl_enc.fit(xtrain[cato_features])
    # xtrain_cat = lbl_enc.transform(xtrain[cato_features])

    # read in data
    SavetoExcel()
    # dtrain = xgb.DMatrix(xtrain,label=y_train)
    dtrain = xgb.DMatrix('C:\\Users\\anran\\xgboost\\demo\\data\\agaricus.txt.train')

    dtest = xgb.DMatrix('C:\\Users\\anran\\xgboost\\demo\\data\\agaricus.txt.test')
    # specify parameters via map
    param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' }
    num_round = 2
    bst = xgb.train(param, dtrain, num_round)
    # make prediction
    preds = bst.predict(dtest)
    # bst.save_model('0001.model')
    bst.dump_model('dump.raw.txt')
    #print(preds)