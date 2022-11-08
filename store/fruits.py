import pandas as pd
def new_fruits_df():
    dc = {}

    #df = pd.DataFrame(dc)
    ls1 = ['제품','가격','판매량'] #스키마 , 키
    ls2 = ['사과', '딸기','수박'] # 제품 , 벨류
    ls3 = [1800, 1500, 3000] # 가격, 벨류
    ls4 = [24, 38, 13] # 판매량, 벨류
    ls5 = [ls2,ls3,ls4]

    for i,j in enumerate(ls1): #중요
        dc[j]= ls5[i]


    df = pd.DataFrame.from_dict(dc)
    print(df)

if __name__ == '__main__':
    new_fruits_df()


