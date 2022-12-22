import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
#matplotlib 패키지 한글 깨짐 처리 시작
import matplotlib.pyplot as plt
import plotly.express as px
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin' :
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows' :
    path = 'C:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Linux' :
    rc('font', family='NanumGothic')
else:
    print('Unknown system')




df = pd.read_csv('naver.csv')
df.rename(columns = {'title' : '제목'}, inplace = True)
df.rename(columns = {'author' : '작가'}, inplace = True)
df.rename(columns = {'genre' : '장르'}, inplace = True)
df.rename(columns = {'description' : '줄거리'}, inplace = True)
df.rename(columns = {'age' : '연령'}, inplace = True)
df.rename(columns = {'completed' : '완결 여부'}, inplace = True)
df.rename(columns = {'free' : '무료 여부'}, inplace = True)
df.rename(columns = {'rating' : '별점'}, inplace = True)
df_split = df['장르'].str.split(',')
df5 = df.loc[df['연령'] == '전체연령가', ]
df6 = df.loc[df['연령'] == '12세 이용가', ]
df7 = df.loc[df['연령'] == '15세 이용가', ]
df8 = df.loc[df['연령'] == '18세 이용가']
df_g1 = df.loc[df['장르'].str.contains('스토리'), ]
df_g2 = df.loc[df['장르'].str.contains('옴니버스'), ]
df_g3 = df.loc[df['장르'].str.contains('에피소드'), ]
df_1 = df.loc[df['장르'].str.contains('판타지'), ]
df_2 = df.loc[df['장르'].str.contains('스포츠'), ]
df_3 = df.loc[df['장르'].str.contains('개그'), ]
df_4 = df.loc[df['장르'].str.contains('스릴러'), ]
df_5 = df.loc[df['장르'].str.contains('드라마'), ]
df_6 = df.loc[df['장르'].str.contains('액션'), ]
df_7 = df.loc[df['장르'].str.contains('일상'), ]
df_8 = df.loc[df['장르'].str.contains('무협'), ]
df_9 = df.loc[df['장르'].str.contains('감성'), ]
df_10 = df.loc[df['장르'].str.contains('로맨스'), ]



def run_eda_app() : 
    st.title('웹툰을 여러가지 기준으로 분석')
    st.subheader('형식, 연령가, 장르 기준으로 별점의 평균 보기')
    rating = st.selectbox('형식을 선택해주세요.',['선택안함','스토리','옴니버스','에피소드'])
    if rating == '선택안함' :
        pass
    elif rating == '스토리' :
        st.write('스토리 형식의 평균 별점은' , df_g1['별점'].mean() ,'입니다.')
    elif rating == '옴니버스' :
        st.write('옴니버스 형식의 평균 별점은' , df_g2['별점'].mean() ,'입니다.')
    elif rating == '에피소드' :
        st.write('옴니버스 형식의 평균 별점은' , df_g3['별점'].mean() ,'입니다.')

    rating2 = st.selectbox('연령가를 선택해주세요.',['선택안함','전체 연령가','12세 이용가', '15세 이용가' , '18세 이용가'])
    
    if rating2 == '선택안함' :
        pass
    elif rating2 =='전체 연령가' :
        st.write('전체연령가의 평균 별점은',df5['별점'].mean(),'입니다.')
    elif rating2 =='12세 이용가' :
        st.write('12세 이용가의 평균 별점은',df6['별점'].mean(),'입니다.')
    elif rating2 =='15세 이용가' :
        st.write('15세 이용가의 평균 별점은',df7['별점'].mean(),'입니다.')
    elif rating2 =='18세 이용가' :
        st.write('18세 이용가의 평균별점은', df8['별점'].mean(),'입니다')
    
    rating3 = st.selectbox('장르를 선택해주세요.',['선택안함','판타지','스포츠','개그','스릴러','드라마','액션','일상','무협/사극','감성'])
    if rating3 == '선택안함' :
        pass
    elif rating3 == '판타지' :
        st.write('판타지 장르의 평균 별점은',df_1['별점'].mean(),'입니다.')
    elif rating3 == '스포츠' :
        st.write('스포츠 장르의 평균 별점은',df_2['별점'].mean(),'입니다.')
    elif rating3 == '개그' :
        st.write('개그 장르의 평균 별점은',df_3['별점'].mean(),'입니다.')
    elif rating3 == '스릴러' :
        st.write('스릴러 장르의 평균 별점은',df_4['별점'].mean(),'입니다.')
    elif rating3 == '드라마' :
        st.write('드라마 장르의 평균 별점은',df_5['별점'].mean(),'입니다.')
    elif rating3 == '액션' :
        st.write('액션 장르의 평균 별점은',df_6['별점'].mean(),'입니다.')
    elif rating3 == '일상' :
        st.write('일상 장르의 평균 별점은',df_7['별점'].mean(),'입니다.')
    elif rating3 == '무협/사극' :
        st.write('무협/사극 장르의 평균 별점은',df_8['별점'].mean(),'입니다.')
    elif rating3 == '감성' :
        st.write('감성 장르의 평균 별점은',df_9['별점'].mean(),'입니다.')
    elif rating3 == '로맨스' :
        st.write('로맨스 장르의 평균 별점은',df_10['별점'].mean(),'입니다.')
    
    
    
    
    
    st.subheader('웹툰 형식에 따른 작품 개수 비율')
    
    fig1 = plt.figure()
    plt.pie(df_split.str.get(0).value_counts(), autopct='%.1f', startangle = 90,wedgeprops= {'width' : 0.7})
    plt.legend(['스토리','에피소드','옴니버스'])
    plt.title('웹툰 형식')
    st.pyplot(fig1)
    
    
    st.subheader('웹툰 연령가에 따른 작품 개수 비율')
    fig3 = plt.figure()
    plt.pie(df['연령'].value_counts(), autopct='%.1f', startangle = 90)
    plt.legend(['전체 연령가','15세 이용가' , '12세 이용가', '18세 이용가'])
    plt.title('이용가능 연령 비율')
    st.pyplot(fig3)
    
    st.subheader('장르에 따른 작품 개수 비율')
    fig2=px.bar(df_split.str.get(1).value_counts(),title='장르별 작품 개수')
    st.plotly_chart(fig2)

    

    
    
    