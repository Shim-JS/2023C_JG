import streamlit as st
import altair as alt               ##https://altair-viz.github.io/
import plotly.express as px

st.title('대통령 지지율 예측기')

#--------------------------------------------------------
# 데이터 로드
import pandas as pd
df = pd.read_csv("data_clean.csv",encoding = 'cp949')

# 모델 로드
import joblib


#--------------------------------------------------------
# 현재 날짜 출력
import datetime
st.header(f'현재날짜 : {datetime.datetime.now().date()}')
tab1, tab2, tab3, tab4 = st.tabs(['지난주 지지율', '다음 지지율 예측(건수)','다음 지지율 예측(%)', '지지율 검색'])

#--------------------------------------------------------
with tab1:
    
        # 1주전 지지율 확인
    #--------------------------------------------------------
    with st.container():
        past_week_df = df.iloc[-1,:]
        past_year = past_week_df['연도']
        past_month = past_week_df['월']
        past_week = past_week_df['주차']
        past_positive = past_week_df['긍정']
        past_npositive = past_week_df['부정']
        past_non = past_week_df['잘모름']

        # 2주전 뉴스 건수 및 지지율 확인
        past_week_df2 = df.iloc[-2,:]
        past_year2 = past_week_df2['연도']
        past_month2 = past_week_df2['월']
        past_week2 = past_week_df2['주차']
        past_positive2 = past_week_df2['긍정']
        past_npositive2 = past_week_df2['부정']
        past_non2 = past_week_df2['잘모름']

    # st.table(past_week_df)

        st.subheader(f"{int(past_year)}년 {int(past_month)}월 {int(past_week)}주차")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                label = "긍정 지지율",
                value = f"{past_positive}%",
                delta= f"{past_positive - past_positive2}%"
            )

        with col2:
            st.metric(
                label = "부정 지지율",
                value = f"{past_npositive}%",
                delta= f"{past_npositive - past_npositive2}%"
            )

        with col3:
            st.metric(
                label = "무응답",
                value = f"{past_non}%",
                delta= f"{past_non - past_non2}%"
            )

#--------------------------------------------------------
# 1주전 뉴스 건수 확인
#--------------------------------------------------------
    with st.container():
        #구분선 긋기
        st.write('-' * 50)
        
        # ------------------------------------------------------
        ## 데이터 준비
        past_science = past_week_df["과학_IT"]
        past_economic = past_week_df["경제"]
        past_global = past_week_df["국제"]
        #
        past_north_korea = past_week_df["북한_외교"]
        past_culture = past_week_df["문화"]
        past_social = past_week_df["사회"]
        #
        past_issue = past_week_df["사건_사고"]
        past_politic = past_week_df["정치"]
        past_sports = past_week_df["스포츠"]
        #
        past_local = past_week_df["지역"]
        past_etc = past_week_df["기타(날씨, 미분류)"]
        
        # ------------------------------------------------------
        ## 데이터 준비
        past_science_p = past_week_df2["과학_IT"]
        past_economic_p = past_week_df2["경제"]
        past_global_p = past_week_df2["국제"]
        #
        past_north_korea_p = past_week_df2["북한_외교"]
        past_culture_p = past_week_df2["문화"]
        past_social_p = past_week_df2["사회"]
        #
        past_issue_p = past_week_df2["사건_사고"]
        past_politic_p = past_week_df2["정치"]
        past_sports_p = past_week_df2["스포츠"]
        #
        past_local_p = past_week_df2["지역"]
        past_etc_p = past_week_df2["기타(날씨, 미분류)"]
        
        past_week_df_plot = df.iloc[-1, 6 : 16].T.reset_index()
        past_week_df_plot.columns = ["names","values"]
        
        fig1 = px.pie(past_week_df_plot, values='values', names='names', title='뉴스 비율')     
        st.plotly_chart(fig1)
        
        data1, data2, data3, data4 = st.columns([0.25, 0.25, 0.25, 0.25])
      
        with data1 :
            st.metric(
                label = "과학_IT",
                value = f"{int(past_science)}건",
                delta= f"{int(past_science - past_science_p)}건"
            )
            
            st.metric(
                label = "경제",
                value = f"{int(past_economic)}건",
                delta= f"{int(past_economic - past_economic_p)}건"
            )
            
            st.metric(
                label = "국제",
                value = f"{int(past_global)}건",
                delta= f"{int(past_global - past_global_p)}건"
            )
            
        with data2 :
            st.metric(
                label = "북한_외교",
                value = f"{int(past_north_korea)}건",
                delta= f"{int(past_north_korea - past_north_korea_p)}건"
            )
            
            st.metric(
                label = "문화",
                value = f"{int(past_culture)}건",
                delta= f"{int(past_culture - past_culture_p)}건"
            )
            
            st.metric(
                label = "사회",
                value = f"{int(past_social)}건",
                delta= f"{int(past_social - past_social_p)}건"
            )
            
        with data3 :
            st.metric(
                label = "사건_사고",
                value = f"{int(past_issue)}건",
                delta= f"{int(past_issue - past_issue_p)}건"
            )
            
            st.metric(
                label = "정치",
                value = f"{int(past_politic)}건",
                delta= f"{int(past_politic - past_politic_p)}건"
            )
            
            st.metric(
                label = "스포츠",
                value = f"{int(past_sports)}건",
                delta= f"{int(past_sports - past_sports_p)}건"
            )
        
        with data4 :        
            st.metric(
                label = "지역",
                value = f"{int(past_local)}건",
                delta= f"{int(past_local - past_local_p)}건"
            )
            
            st.metric(
                label = "기타(날씨, 미분류)",
                value = f"{int(past_etc)}건",
                delta= f"{int(past_etc - past_etc_p)}건"
            )
            
with tab2:
    with st.container():
        
        st.subheader(f"1. 모델 선택")
        ## 모델 로드 5가지
        model_svm = joblib.load('model/svm_model.pkl')
        model_ebm = joblib.load('model/ebm_model.pkl')
        model_lgbm = joblib.load('model/lgbm_model.pkl')
        model_lr = joblib.load('model/lr_model.pkl')
        model_rf = joblib.load('model/rf_model.pkl')


        model_num = 0
        model_list = [model_lr, model_lgbm, model_rf, model_ebm, model_svm]
        
        model_nm_list = [
            "예측 성능 1위. Linear Regressor Model",
            "예측 성능 2위. LightGBM Regressor Model",
            "예측 성능 3위. RandomForest Regressor Model",
            "예측 성능 4위. ExplainableBoosting Regressor Model",
            "예측 성능 5위. SVM Regressor Model"
        ]
        
        model_error_list = [
            "약 +- 2.0566 정도의 오차가 있습니다.",
            "약 +- 2.1920 정도의 오차가 있습니다.",
            "약 +- 2.3906 정도의 오차가 있습니다.",
            "약 +- 2.7810 정도의 오차가 있습니다.",
            "약 +- 7.751 정도의 오차가 있습니다."
        ]
        select_model = st.selectbox(
        '원하는 예측 모델을 고르세요.',
        model_nm_list
         )
        
        if select_model == model_nm_list[0]:
            model_num = 0
        elif select_model == model_nm_list[1]:
            model_num = 1
        elif select_model == model_nm_list[2]:
            model_num = 2
        elif select_model == model_nm_list[3]:
            model_num = 3
        elif select_model == model_nm_list[4]:
            model_num = 4
        
        st.divider()
        
        st.subheader(f"2. 뉴스 데이터 입력")
        data1, data2, data3, data4 = st.columns([0.25, 0.25, 0.25, 0.25])
        
        with data1 :
            write_science = st.number_input(
                label = "과학_IT",
                value = 0,
                placeholder = f"{int(past_science)}건",
            )
            
            write_economic = st.number_input(
                label = "경제",
                value = 0,
                placeholder = f"{int(past_economic)}건",
            )
            
            write_global = st.number_input(
                label = "국제",
                value = 0,
                placeholder = f"{int(past_global)}건",
            )
            
        with data2 :
            write_north_korea = st.number_input(
                label = "북한_외교",
                value = 0,
                placeholder = f"{int(past_north_korea)}건",
            )
            
            write_culture = st.number_input(
                label = "문화",
                value = 0,
                placeholder = f"{int(past_culture)}건",
            )
            
            write_social = st.number_input(
                label = "사회",
                value = 0,
                placeholder = f"{int(past_social)}건",
            )
            
        with data3 :
            write_issue = st.number_input(
                label = "사건_사고",
                value = 0,
                placeholder = f"{int(past_issue)}건",
            )
            
            write_politic = st.number_input(
                label = "정치",
                value = 0,
                placeholder = f"{int(past_politic)}건",
            )
            
            write_sports = st.number_input(
                label = "스포츠",
                value = 0,
                placeholder = f"{int(past_sports)}건",
            )
        
        with data4 :        
            write_local = st.number_input(
                label = "지역",
                value = 0,
                placeholder = f"{int(past_local)}건",
            )
            
            write_etc = st.number_input(
                label = "기타(날씨, 미분류)",
                value = 0,
                placeholder = f"{int(past_etc)}건",
            )
            
        ## 버튼 클릭
        if st.button('**지지율 예측 시작!**'):
            st.divider()
            st.subheader(f"3. 다음주 지지율 예측", divider='rainbow')
            st.text("다음 지지율을 예측합니다.")
            
            ## ========================= 학습 데이터 구축========================= ##
            write_df_past = pd.DataFrame(df.iloc[-1]).T.reset_index(drop = True)
            write_df_new = pd.DataFrame(df.iloc[-1]).T.reset_index(drop = True).drop(["연도","월","주차", "긍정", "부정", "잘모름"], axis = 1)
            
            write_df_new.loc[0,'긍정_과거'] = write_df_past.loc[0,'긍정']
            write_df_new.loc[0,'부정_과거'] = write_df_past.loc[0,'부정']
            write_df_new.loc[0,'잘모름_과거'] = write_df_past.loc[0,'잘모름']
            
            write_df_new.loc[0,'과학_IT'] = write_science
            write_df_new.loc[0,'경제'] = write_economic
            write_df_new.loc[0,'국제'] = write_global
            write_df_new.loc[0,'북한_외교'] = write_north_korea
            write_df_new.loc[0,'문화'] = write_culture
            write_df_new.loc[0,'사회'] = write_social
            write_df_new.loc[0,'사건_사고'] = write_issue
            write_df_new.loc[0,'정치'] = write_politic
            write_df_new.loc[0,'스포츠'] = write_sports
            write_df_new.loc[0,'지역'] = write_local
            write_df_new.loc[0,'기타(날씨, 미분류)'] = write_etc
            
            sum_news = sum([write_science, write_economic, write_global, write_north_korea,
              write_culture, write_social, write_issue, write_politic,
              write_sports, write_local, write_etc])

            write_df_new.loc[0,'과학_IT%'] = (write_science/sum_news) *100
            write_df_new.loc[0,'경제%'] = (write_economic/sum_news) *100
            write_df_new.loc[0,'국제%'] = (write_global/sum_news) *100
            write_df_new.loc[0,'북한_외교%'] = (write_north_korea/sum_news) *100
            write_df_new.loc[0,'문화%'] = (write_culture/sum_news) *100
            write_df_new.loc[0,'사회%'] = (write_social/sum_news) *100
            write_df_new.loc[0,'사건_사고%'] = (write_issue/sum_news) *100
            write_df_new.loc[0,'정치%'] = (write_politic/sum_news) *100
            write_df_new.loc[0,'스포츠%'] = (write_sports/sum_news) *100
            write_df_new.loc[0,'지역%'] = (write_local/sum_news) *100
            write_df_new.loc[0,'기타(날씨, 미분류)%'] = (write_etc/sum_news) *100
            
            write_df_new.loc[0,'과학_IT_증감량'] = write_df_new.loc[0,'과학_IT'] - write_df_past.loc[0,'과학_IT']
            write_df_new.loc[0,'경제_증감량'] = write_df_new.loc[0,'경제'] - write_df_past.loc[0,'경제']
            write_df_new.loc[0,'국제_증감량'] = write_df_new.loc[0,'국제'] - write_df_past.loc[0,'국제']
            write_df_new.loc[0,'북한_외교_증감량'] = write_df_new.loc[0,'북한_외교'] - write_df_past.loc[0,'북한_외교']
            write_df_new.loc[0,'문화_증감량'] = write_df_new.loc[0,'문화'] - write_df_past.loc[0,'문화']
            write_df_new.loc[0,'사회_증감량'] = write_df_new.loc[0,'사회'] - write_df_past.loc[0,'사회']
            write_df_new.loc[0,'사건_사고_증감량'] = write_df_new.loc[0,'사건_사고'] - write_df_past.loc[0,'사건_사고']
            write_df_new.loc[0,'정치_증감량'] = write_df_new.loc[0,'정치'] - write_df_past.loc[0,'정치']
            write_df_new.loc[0,'스포츠_증감량'] = write_df_new.loc[0,'스포츠'] - write_df_past.loc[0,'스포츠']
            write_df_new.loc[0,'지역_증감량'] = write_df_new.loc[0,'지역'] - write_df_past.loc[0,'지역']
            write_df_new.loc[0,'기타(날씨, 미분류)_증감량'] = write_df_new.loc[0,'기타(날씨, 미분류)'] - write_df_past.loc[0,'기타(날씨, 미분류)']
            
            X_test = pd.DataFrame(write_df_new.loc[0,['긍정_과거', '부정_과거', '잘모름_과거','과학_IT', '경제', '국제', '북한_외교', '문화',
       '사회', '사건_사고', '정치', '스포츠', '지역', '기타(날씨, 미분류)', '주간합', '과학_IT%', '경제%',
       '국제%', '북한_외교%', '문화%', '사회%', '사건_사고%', '정치%', '스포츠%', '지역%', '기타(날씨, 미분류)%',
         '과학_IT_증감량', '경제_증감량', '국제_증감량', '북한_외교_증감량', '문화_증감량', '사회_증감량', '사건_사고_증감량', '정치_증감량',
       '스포츠_증감량', '지역_증감량', '기타(날씨, 미분류)_증감량']]).T
            
            ## ========================= 학습 데이터 구축========================= ##
            
            ## 예측 ##
            
            st.table(X_test)
            
            pred_score = model_list[model_num].predict(X_test)
            
            st.subheader(f"_다음 긍정 지지율 예측값은_ :blue[{pred_score}%] 입니다. 😄   (:red[{model_error_list[model_num]}])")
            
            
with tab3:
    with st.container():
        
        st.subheader(f"1. 모델 선택")
        ## 모델 로드 5가지
        model_svm = joblib.load('model/svm_model.pkl')
        model_ebm = joblib.load('model/ebm_model.pkl')
        model_lgbm = joblib.load('model/lgbm_model.pkl')
        model_lr = joblib.load('model/lr_model.pkl')
        model_rf = joblib.load('model/rf_model.pkl')

        model_num = 0
        model_list2 = [model_lr, model_lgbm, model_rf, model_ebm, model_svm]
        
        model_nm_list = [
            "예측 성능 1위. Linear Regressor Model",
            "예측 성능 2위. LightGBM Regressor Model",
            "예측 성능 3위. RandomForest Regressor Model",
            "예측 성능 4위. ExplainableBoosting Regressor Model",
            "예측 성능 5위. SVM Regressor Model"
        ]
        
        model_error_list = [
            "약 +- 2.0566 정도의 오차가 있습니다.",
            "약 +- 2.1920 정도의 오차가 있습니다.",
            "약 +- 2.3906 정도의 오차가 있습니다.",
            "약 +- 2.7810 정도의 오차가 있습니다.",
            "약 +- 7.751 정도의 오차가 있습니다."
        ]
        select_model = st.selectbox(
        '원하는 예측 모델을 고르세요!',
        model_nm_list
         )
        
        if select_model == model_nm_list[0]:
            model_num = 0
        elif select_model == model_nm_list[1]:
            model_num = 1
        elif select_model == model_nm_list[2]:
            model_num = 2
        elif select_model == model_nm_list[3]:
            model_num = 3
        elif select_model == model_nm_list[4]:
            model_num = 4
            
            
            
        st.divider()
        
        st.subheader(f"2. 뉴스 데이터 (%) 입력")
        data1, data2, data3, data4 = st.columns([0.25, 0.25, 0.25, 0.25])
        
        total_news = 11000
        
        with data1 :
            write_science = st.number_input(
                label = "과학_IT(%)",
                value = 0.00,
                placeholder = f"{int(past_science)/100}(%)",
            )
            
            write_economic = st.number_input(
                label = "경제(%)",
                value = 0.00,
                placeholder = f"{int(past_economic)/100}(%)",
            )
            
            write_global = st.number_input(
                label = "국제(%)",
                value = 0.00,
                placeholder = f"{int(past_global)/100}(%)",
            )
            
        with data2 :
            write_north_korea = st.number_input(
                label = "북한_외교(%)",
                value = 0.00,
                placeholder = f"{int(past_north_korea)/100}(%)",
            )
            
            write_culture = st.number_input(
                label = "문화(%)",
                value = 0.00,
                placeholder = f"{int(past_culture)/100}(%)",
            )
            
            write_social = st.number_input(
                label = "사회(%)",
                value = 0.00,
                placeholder = f"{int(past_social)/100}(%)",
            )
            
        with data3 :
            write_issue = st.number_input(
                label = "사건_사고(%)",
                value = 0.00,
                placeholder = f"{int(past_issue)/100}(%)",
            )
            
            write_politic = st.number_input(
                label = "정치(%)",
                value = 0.00,
                placeholder = f"{int(past_politic)/100}(%)",
            )
            
            write_sports = st.number_input(
                label = "스포츠(%)",
                value = 0.00,
                placeholder = f"{int(past_sports)/100}(%)",
            )
        
        with data4 :        
            write_local = st.number_input(
                label = "지역(%)",
                value = 0.00,
                placeholder = f"{int(past_local)/100}(%)",
            )
            
            write_etc = st.number_input(
                label = "기타(날씨, 미분류)(%)",
                value = 0.00,
                placeholder = f"{int(past_etc)/100}(%)",
            )
            
        ## 버튼 클릭
        if st.button('**!지지율 예측 시작!**'):
            st.divider()
            st.subheader(f"3. 다음주 지지율 예측", divider='rainbow')
            st.text("다음 지지율을 예측합니다.")
            
            ## ========================= 학습 데이터 구축========================= ##
            write_df_past = pd.DataFrame(df.iloc[-1]).T.reset_index(drop = True)
            write_df_new = pd.DataFrame(df.iloc[-1]).T.reset_index(drop = True).drop(["연도","월","주차", "긍정", "부정", "잘모름"], axis = 1)
            
            write_df_new.loc[0,'긍정_과거'] = write_df_past.loc[0,'긍정']
            write_df_new.loc[0,'부정_과거'] = write_df_past.loc[0,'부정']
            write_df_new.loc[0,'잘모름_과거'] = write_df_past.loc[0,'잘모름']
            
            write_df_new.loc[0,'과학_IT'] = write_science * total_news / 100
            write_df_new.loc[0,'경제'] = write_economic * total_news / 100
            write_df_new.loc[0,'국제'] = write_global * total_news / 100
            write_df_new.loc[0,'북한_외교'] = write_north_korea * total_news / 100
            write_df_new.loc[0,'문화'] = write_culture * total_news / 100
            write_df_new.loc[0,'사회'] = write_social * total_news / 100
            write_df_new.loc[0,'사건_사고'] = write_issue * total_news / 100
            write_df_new.loc[0,'정치'] = write_politic * total_news / 100
            write_df_new.loc[0,'스포츠'] = write_sports * total_news / 100
            write_df_new.loc[0,'지역'] = write_local * total_news / 100
            write_df_new.loc[0,'기타(날씨, 미분류)'] = write_etc * total_news / 100
            sum_news = sum([write_science, write_economic, write_global, write_north_korea,
              write_culture, write_social, write_issue, write_politic,
              write_sports, write_local, write_etc])
            write_df_new.loc[0,'주간합'] = sum_news * total_news / 100

            write_df_new.loc[0,'과학_IT%'] = write_science
            write_df_new.loc[0,'경제%'] = write_economic
            write_df_new.loc[0,'국제%'] = write_global
            write_df_new.loc[0,'북한_외교%'] = write_north_korea
            write_df_new.loc[0,'문화%'] = write_culture
            write_df_new.loc[0,'사회%'] = write_social
            write_df_new.loc[0,'사건_사고%'] = write_issue
            write_df_new.loc[0,'정치%'] = write_politic
            write_df_new.loc[0,'스포츠%'] = write_sports
            write_df_new.loc[0,'지역%'] = write_local
            write_df_new.loc[0,'기타(날씨, 미분류)%'] = write_etc
            
            write_df_new.loc[0,'과학_IT_증감량'] = write_df_new.loc[0,'과학_IT'] - write_df_past.loc[0,'과학_IT']
            write_df_new.loc[0,'경제_증감량'] = write_df_new.loc[0,'경제'] - write_df_past.loc[0,'경제']
            write_df_new.loc[0,'국제_증감량'] = write_df_new.loc[0,'국제'] - write_df_past.loc[0,'국제']
            write_df_new.loc[0,'북한_외교_증감량'] = write_df_new.loc[0,'북한_외교'] - write_df_past.loc[0,'북한_외교']
            write_df_new.loc[0,'문화_증감량'] = write_df_new.loc[0,'문화'] - write_df_past.loc[0,'문화']
            write_df_new.loc[0,'사회_증감량'] = write_df_new.loc[0,'사회'] - write_df_past.loc[0,'사회']
            write_df_new.loc[0,'사건_사고_증감량'] = write_df_new.loc[0,'사건_사고'] - write_df_past.loc[0,'사건_사고']
            write_df_new.loc[0,'정치_증감량'] = write_df_new.loc[0,'정치'] - write_df_past.loc[0,'정치']
            write_df_new.loc[0,'스포츠_증감량'] = write_df_new.loc[0,'스포츠'] - write_df_past.loc[0,'스포츠']
            write_df_new.loc[0,'지역_증감량'] = write_df_new.loc[0,'지역'] - write_df_past.loc[0,'지역']
            write_df_new.loc[0,'기타(날씨, 미분류)_증감량'] = write_df_new.loc[0,'기타(날씨, 미분류)'] - write_df_past.loc[0,'기타(날씨, 미분류)']
            
            X_test = pd.DataFrame(write_df_new.loc[0,['긍정_과거', '부정_과거', '잘모름_과거','과학_IT', '경제', '국제', '북한_외교', '문화',
       '사회', '사건_사고', '정치', '스포츠', '지역', '기타(날씨, 미분류)', '주간합', '과학_IT%', '경제%',
       '국제%', '북한_외교%', '문화%', '사회%', '사건_사고%', '정치%', '스포츠%', '지역%', '기타(날씨, 미분류)%',
         '과학_IT_증감량', '경제_증감량', '국제_증감량', '북한_외교_증감량', '문화_증감량', '사회_증감량', '사건_사고_증감량', '정치_증감량',
       '스포츠_증감량', '지역_증감량', '기타(날씨, 미분류)_증감량']]).T
            
            ## ========================= 학습 데이터 구축========================= ##
            
            ## 예측 ##
            
            st.table(X_test)
            X_test.to_csv("temp.csv",index = False, encoding = 'cp949')
            
            pred_score = model_list2[model_num].predict(X_test)
            
            st.subheader(f"_다음 긍정 지지율 예측값은_ :blue[{pred_score}%] 입니다. 😄   (:red[{model_error_list[model_num]}])")

            
#--------------------------------------------------------
with tab4:
            # 1주전 지지율 확인
    #--------------------------------------------------------
    with st.container():
        past_week_df_select = past_week_df
        past_week_df_select2 = past_week_df2
        
        
        select1, select2, select3 =  st.columns(3)

        ## 리스트 반환
        year_list = sorted(df.연도.unique(),reverse=True)
        month_list = sorted(df.월.unique(),reverse=True)
        week_list = sorted(df.주차.unique(),reverse=True)
        with select1:
            select_year = st.selectbox(
            '원하는 검색 연도를 고르세요.',
            year_list
            )
            
        with select2:
            select_month = st.selectbox(
            '원하는 검색 달을 고르세요.',
            month_list
            )
        
        with select3:
            select_week = st.selectbox(
            '원하는 검색 주차를 고르세요.',
            week_list
            )
            
        try:
            if st.button('**지지율 검색!**'):

                st.divider()

                past_week_df_select = pd.DataFrame(df[(df.연도 == select_year) & (df.월 == select_month) & (df.주차 == select_week)])

                select_index = past_week_df_select.index.values[0]


                past_year_select = past_week_df_select['연도']
                past_month_select = past_week_df_select['월'].values[0]
                past_week_select = past_week_df_select['주차'].values[0]
                past_positive_select = past_week_df_select['긍정'].values[0]
                past_npositive_select = past_week_df_select['부정'].values[0]
                past_non_select = past_week_df_select['잘모름'].values[0]


                # 2주전 뉴스 건수 및 지지율 확인
                past_week_df_select2 = pd.DataFrame(df.loc[select_index-1,:]).T

                past_year_select2 = past_week_df_select2['연도'].values[0]
                past_month_select2 = past_week_df_select2['월'].values[0]
                past_week_select2 = past_week_df_select2['주차'].values[0]
                past_positive_select2 = past_week_df_select2['긍정'].values[0]
                past_npositive_select2 = past_week_df_select2['부정'].values[0]
                past_non_select2 = past_week_df_select2['잘모름'].values[0]

                st.subheader(f"{int(past_year_select)}년 {int(past_month_select)}월 {int(past_week_select)}주차")

                select_col1, select_col2, select_col3 = st.columns(3)

                with select_col1:
                    st.metric(
                        label = "긍정 지지율",
                        value = f"{past_positive_select}%",
                        delta= f"{past_positive_select - past_positive_select2}%"
                    )

                with select_col2:
                    st.metric(
                        label = "부정 지지율",
                        value = f"{past_npositive_select}%",
                        delta= f"{past_npositive_select - past_npositive_select2}%"
                    )

                with select_col3:
                    st.metric(
                        label = "무응답",
                        value = f"{past_non_select}%",
                        delta= f"{past_non_select - past_non_select2}%"
                    )

        #--------------------------------------------------------
        # 1주전 뉴스 건수 확인
        #--------------------------------------------------------
            with st.container():
                #구분선 긋기
                st.write('-' * 50)

                # ------------------------------------------------------
                ## 데이터 준비
                past_science_select = past_week_df_select["과학_IT"].values[0]
                past_economic_select = past_week_df_select["경제"].values[0]
                past_global_select = past_week_df_select["국제"].values[0]
                #
                past_north_korea_select = past_week_df_select["북한_외교"].values[0]
                past_culture_select = past_week_df_select["문화"].values[0]
                past_social_select = past_week_df_select["사회"].values[0]
                #
                past_issue_select = past_week_df_select["사건_사고"].values[0]
                past_politic_select = past_week_df_select["정치"].values[0]
                past_sports_select = past_week_df_select["스포츠"].values[0]
                #
                past_local_select = past_week_df_select["지역"].values[0]
                past_etc_select = past_week_df_select["기타(날씨, 미분류)"].values[0]

                # ------------------------------------------------------
                ## 데이터 준비
                past_science_p_select = past_week_df_select2["과학_IT"].values[0]
                past_economic_p_select = past_week_df_select2["경제"].values[0]
                past_global_p_select = past_week_df_select2["국제"].values[0]
                #
                past_north_korea_p_select = past_week_df_select2["북한_외교"].values[0]
                past_culture_p_select = past_week_df_select2["문화"].values[0]
                past_social_p_select = past_week_df_select2["사회"].values[0]
                #
                past_issue_p_select = past_week_df_select2["사건_사고"].values[0]
                past_politic_p_select = past_week_df_select2["정치"].values[0]
                past_sports_p_select = past_week_df_select2["스포츠"].values[0]
                #
                past_local_p_select = past_week_df_select2["지역"].values[0]
                past_etc_p_select = past_week_df_select2["기타(날씨, 미분류)"].values[0]

                past_week_df_plot2 = past_week_df_select.iloc[-1, 6 : 16].T.reset_index()
                past_week_df_plot2.columns = ["names","values"]

                fig1 = px.pie(past_week_df_plot2, values='values', names='names', title='뉴스 비율')     
                st.plotly_chart(fig1)

                data_select1, data_select2, data_select3, data_select4 = st.columns([0.25, 0.25, 0.25, 0.25])

                with data_select1 :
                    st.metric(
                        label = "과학_IT",
                        value = f"{int(past_science_select)}건",
                        delta= f"{int(past_science_select - past_science_p_select)}건"
                    )

                    st.metric(
                        label = "경제",
                        value = f"{int(past_economic_select)}건",
                        delta= f"{int(past_economic_select - past_economic_p_select)}건"
                    )

                    st.metric(
                        label = "국제",
                        value = f"{int(past_global_select)}건",
                        delta= f"{int(past_global_select - past_global_p_select)}건"
                    )

                with data_select2 :
                    st.metric(
                        label = "북한_외교",
                        value = f"{int(past_north_korea_select)}건",
                        delta= f"{int(past_north_korea_select - past_north_korea_p_select)}건"
                    )

                    st.metric(
                        label = "문화",
                        value = f"{int(past_culture_select)}건",
                        delta= f"{int(past_culture_select - past_culture_p_select)}건"
                    )

                    st.metric(
                        label = "사회",
                        value = f"{int(past_social_select)}건",
                        delta= f"{int(past_social_select - past_social_p_select)}건"
                    )

                with data_select3 :
                    st.metric(
                        label = "사건_사고",
                        value = f"{int(past_issue_select)}건",
                        delta= f"{int(past_issue_select - past_issue_p_select)}건"
                    )

                    st.metric(
                        label = "정치",
                        value = f"{int(past_politic_select)}건",
                        delta= f"{int(past_politic_select - past_politic_p_select)}건"
                    )

                    st.metric(
                        label = "스포츠",
                        value = f"{int(past_sports_select)}건",
                        delta= f"{int(past_sports_select - past_sports_p_select)}건"
                    )

                with data_select4 :        
                    st.metric(
                        label = "지역",
                        value = f"{int(past_local_select)}건",
                        delta= f"{int(past_local_select - past_local_p_select)}건"
                    )

                    st.metric(
                        label = "기타(날씨, 미분류)",
                        value = f"{int(past_etc_select)}건",
                        delta= f"{int(past_etc_select - past_etc_p_select)}건"
                    )

        except : 
            st.subheader("값을 입력해주세요.")

            
            
                                
            
            
        
        
        
    