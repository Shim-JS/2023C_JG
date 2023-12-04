import pandas as pd

# 데이터 로드
df = pd.read_csv("data_clean.csv",encoding = 'cp949')

## 미조사 데이터 제외
df_clean = df.loc[df['긍정'] != 0]
df_clean = df_clean.reset_index(drop = True)

## 전월 긍정_부정_잘모름 열 추가
for i in range(1,len(df_clean)):
    df_clean.loc[i,'긍정_과거'] = df_clean.loc[i-1,'긍정']
    df_clean.loc[i,'부정_과거'] = df_clean.loc[i-1,'부정']
    df_clean.loc[i,'잘모름_과거'] = df_clean.loc[i-1,'잘모름']
    
    ## 뉴스 카테고리별 증감량 열 추가
    df_clean.loc[i,'과학_IT_증감량'] = df_clean.loc[i,'과학_IT'] - df_clean.loc[i-1,'과학_IT']
    df_clean.loc[i,'경제_증감량'] = df_clean.loc[i,'경제'] - df_clean.loc[i-1,'경제']
    df_clean.loc[i,'국제_증감량'] = df_clean.loc[i,'국제'] - df_clean.loc[i-1,'국제']
    df_clean.loc[i,'북한_외교_증감량'] = df_clean.loc[i,'북한_외교'] - df_clean.loc[i-1,'북한_외교']
    df_clean.loc[i,'문화_증감량'] = df_clean.loc[i,'문화'] - df_clean.loc[i-1,'문화']
    df_clean.loc[i,'사회_증감량'] = df_clean.loc[i,'사회'] - df_clean.loc[i-1,'사회']
    df_clean.loc[i,'사건_사고_증감량'] = df_clean.loc[i,'사건_사고'] - df_clean.loc[i-1,'사건_사고']
    df_clean.loc[i,'정치_증감량'] = df_clean.loc[i,'정치'] - df_clean.loc[i-1,'정치']
    df_clean.loc[i,'스포츠_증감량'] = df_clean.loc[i,'스포츠'] - df_clean.loc[i-1,'스포츠']
    df_clean.loc[i,'지역_증감량'] = df_clean.loc[i,'지역'] - df_clean.loc[i-1,'지역']
    df_clean.loc[i,'기타(날씨, 미분류)_증감량'] = df_clean.loc[i,'기타(날씨, 미분류)'] - df_clean.loc[i-1,'기타(날씨, 미분류)']
    
    
    
df_clean = df_clean.drop(0,axis=0).reset_index(drop = True)

# 학습용 데이터
X_train = df_clean.loc[df_clean['연도'] < 2023,['긍정_과거', '부정_과거', '잘모름_과거', '과학_IT', '경제', '국제', '북한_외교', '문화',
       '사회', '사건_사고', '정치', '스포츠', '지역', '기타(날씨, 미분류)', '주간합', '과학_IT%', '경제%',
       '국제%', '북한_외교%', '문화%', '사회%', '사건_사고%', '정치%', '스포츠%', '지역%', '기타(날씨, 미분류)%',
        '과학_IT_증감량', '경제_증감량', '국제_증감량', '북한_외교_증감량', '문화_증감량', '사회_증감량', '사건_사고_증감량', '정치_증감량',
       '스포츠_증감량', '지역_증감량', '기타(날씨, 미분류)_증감량']]

y_train = df_clean.loc[df_clean['연도'] < 2023,['긍정']]

# y_train = df_clean.loc[df_clean['연도'] < 2022,['부정']]

# 테스트용 데이터
X_test = df_clean.loc[df_clean['연도'] == 2023,['긍정_과거', '부정_과거', '잘모름_과거','과학_IT', '경제', '국제', '북한_외교', '문화',
       '사회', '사건_사고', '정치', '스포츠', '지역', '기타(날씨, 미분류)', '주간합', '과학_IT%', '경제%',
       '국제%', '북한_외교%', '문화%', '사회%', '사건_사고%', '정치%', '스포츠%', '지역%', '기타(날씨, 미분류)%',
         '과학_IT_증감량', '경제_증감량', '국제_증감량', '북한_외교_증감량', '문화_증감량', '사회_증감량', '사건_사고_증감량', '정치_증감량',
       '스포츠_증감량', '지역_증감량', '기타(날씨, 미분류)_증감량']]
y_test = df_clean.loc[df_clean['연도'] == 2023,['긍정']]

# y_test = df_clean.loc[df_clean['연도'] == 2022,['부정']]

y_idx = df_clean.loc[df_clean['연도'] == 2023,['연도', '월', '주차']]



X_train.columns = ["Positive_Past","Negative_Past","Non_Past","Science_IT","Ecnomic","Global","North_Korea","Culture","Social","Issue", 'Politic', 'Sports', 'Local', 'Etc', 'SUM',
                  "Science_IT_P","Ecnomic_P","Global_P","North_Korea_P","Culture_P","Social_P","Issue_P", 'Politic_P', 'Sports_P', 'Local_P', 'Etc_P',
                  "Science_IT_ID","Ecnomic_ID","Global_ID","North_Korea_ID","Culture_ID","Social_ID","Issue_ID", 'Politic_ID', 'Sports_ID', 'Local_ID', 'Etc_ID']
y_train.columns = ['Target']

X_test.columns = ["Positive_Past","Negative_Past","Non_Past","Science_IT","Ecnomic","Global","North_Korea","Culture","Social","Issue", 'Politic', 'Sports', 'Local', 'Etc', 'SUM',
                  "Science_IT_P","Ecnomic_P","Global_P","North_Korea_P","Culture_P","Social_P","Issue_P", 'Politic_P', 'Sports_P', 'Local_P', 'Etc_P',
                  "Science_IT_ID","Ecnomic_ID","Global_ID","North_Korea_ID","Culture_ID","Social_ID","Issue_ID", 'Politic_ID', 'Sports_ID', 'Local_ID', 'Etc_ID']
y_test.columns = ['Target']

from sklearn.linear_model import LinearRegression
lr_model = LinearRegression()

lr_model.fit(X_train,y_train)


from sklearn import svm

svm_model = svm.SVR()

svm_model.fit(X_train, y_train)

from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)


from lightgbm import LGBMRegressor

## 모델링

# lgbm_model = LGBMRegressor(bagging_fraction=0.6, bagging_freq=6, boosting_type='gbdt',
#                class_weight=None, colsample_bytree=1.0, device='gpu',
#                feature_fraction=0.8, importance_type='split', learning_rate=0.05,
#                max_depth=6, min_child_samples=16, min_child_weight=0.001,
#                min_split_gain=0.3, n_estimators=120, n_jobs=-1, num_leaves=150,
#                objective=None, random_state=2021, reg_alpha=1e-06, reg_lambda=10,
#                silent='warn', subsample=1.0, subsample_for_bin=200000,
#                subsample_freq=0)

lgbm_model = LGBMRegressor()
lgbm_model.fit(X_train,y_train)

lgbm_model.score(X_train,y_train)

from interpret.glassbox import ExplainableBoostingRegressor
ebm_model = ExplainableBoostingRegressor()
ebm_model.fit(X_train, y_train)

import pickle
import joblib

model_nm = ['lr', 'svm', 'rf', 'lgbm', 'ebm']

joblib.dump(lr_model, 'model/lr_model.pkl')
joblib.dump(svm_model, 'model/svm_model.pkl')
joblib.dump(rf_model, 'model/rf_model.pkl')
joblib.dump(lgbm_model, 'model/lgbm_model.pkl')
joblib.dump(ebm_model, 'model/ebm_model.pkl')