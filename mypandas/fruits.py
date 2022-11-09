import pandas as pd
def new_fruits_df():
    dc = {}

    #df = pd.DataFrame(dc)
    ls1 = ['제품','가격','판매량'] #스키마 , 키, (상수, 아래는 변수)
    ls2 = ['사과', '딸기','수박'] # 제품 , 벨류
    ls3 = [1800, 1500, 3000] # 가격, 벨류
    ls4 = [24, 38, 13] # 판매량, 벨류
    ls5 = [ls2,ls3,ls4]

    for i,j in enumerate(ls1): #중요
        dc[j]= ls5[i]
        #dc의 리스트의 0번째 벨류는 ls5의 0번째 인덱스

    dc = {j : ls5[i] for i,j in enumerate(ls1)}


    df = pd.DataFrame.from_dict(dc)
    print(df)
    print('가격평균:' + str(df['가격'].mean()))

if __name__ == '__main__':
    new_fruits_df()


