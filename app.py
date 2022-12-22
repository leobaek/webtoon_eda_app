import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from app_drama import run_drama_app
from app_eda import run_eda_app

df = pd.read_csv('naver.csv')
df2 = df.loc[ : ,['title','author','genre','rating','description','age','completed','free']   ]
df3 = df2.sort_values(by='genre',ascending=False)
df4 = df2.sort_values(by='rating', ascending=False)

df3.rename(columns = {'title' : '제목'}, inplace = True)
df3.rename(columns = {'author' : '작가'}, inplace = True)
df3.rename(columns = {'genre' : '장르'}, inplace = True)
df3.rename(columns = {'description' : '줄거리'}, inplace = True)
df3.rename(columns = {'age' : '연령'}, inplace = True)
df3.rename(columns = {'completed' : '완결 여부'}, inplace = True)
df3.rename(columns = {'free' : '무료 여부'}, inplace = True)
df3.rename(columns = {'rating' : '별점'}, inplace = True)
df4.dropna(inplace=True) 
df4.rename(columns = {'title' : '제목'}, inplace = True)
df4.rename(columns = {'author' : '작가'}, inplace = True)
df4.rename(columns = {'genre' : '장르'}, inplace = True)
df4.rename(columns = {'description' : '줄거리'}, inplace = True)
df4.rename(columns = {'age' : '연령'}, inplace = True)
df4.rename(columns = {'completed' : '완결 여부'}, inplace = True)
df4.rename(columns = {'free' : '무료 여부'}, inplace = True)
df4.rename(columns = {'rating' : '별점'}, inplace = True)
df4.dropna(inplace=True)
img_url = 'https://image.zdnet.co.kr/2020/03/06/hjan_EWKpagLviyCwJNQ.jpg'


## 스토리
df_story1 = df4.loc[df3['장르'].str.contains('스토리, 로맨스'), ].reset_index().drop('index', axis=1)
df_story2 = df4.loc[df3['장르'].str.contains('스토리, 판타지'), ].reset_index().drop('index', axis=1)
df_story3 = df4.loc[df3['장르'].str.contains('스토리, 스포츠'), ].reset_index().drop('index', axis=1)
df_story4 = df4.loc[df3['장르'].str.contains('스토리, 개그'), ].reset_index().drop('index', axis=1)
df_story5 = df4.loc[df3['장르'].str.contains('스토리, 스릴러'), ].reset_index().drop('index', axis=1)
df_story6 = df4.loc[df3['장르'].str.contains('스토리, 드라마'), ].reset_index().drop('index', axis=1)
df_story7 = df4.loc[df3['장르'].str.contains('스토리, 액션'), ].reset_index().drop('index', axis=1)
df_story8 = df4.loc[df3['장르'].str.contains('스토리, 일상'), ].reset_index().drop('index', axis=1)
df_story9 = df4.loc[df3['장르'].str.contains('스토리, 무협/사극'), ].reset_index().drop('index', axis=1)
df_story10 = df4.loc[df3['장르'].str.contains('스토리, 감성'), ].reset_index().drop('index', axis=1)

## 스토리

## 옴니버스
df_omnibus1 = df3.loc[df3['장르'].str.contains('옴니버스, 로맨스'), ].reset_index().drop('index', axis=1)
df_omnibus2 = df3.loc[df3['장르'].str.contains('옴니버스, 판타지'), ].reset_index().drop('index', axis=1)
df_omnibus3 = df3.loc[df3['장르'].str.contains('옴니버스, 스포츠'), ].reset_index().drop('index', axis=1)
df_omnibus4 = df3.loc[df3['장르'].str.contains('옴니버스, 개그'), ].reset_index().drop('index', axis=1)
df_omnibus5 = df3.loc[df3['장르'].str.contains('옴니버스, 스릴러'), ].reset_index().drop('index', axis=1)
df_omnibus6 = df3.loc[df3['장르'].str.contains('옴니버스, 드라마'), ].reset_index().drop('index', axis=1)
df_omnibus7 = df3.loc[df3['장르'].str.contains('옴니버스, 액션'), ].reset_index().drop('index', axis=1)
df_omnibus8 = df3.loc[df3['장르'].str.contains('옴니버스, 일상'), ].reset_index().drop('index', axis=1)
df_omnibus9 = df3.loc[df3['장르'].str.contains('옴니버스, 무협/사극'), ].reset_index().drop('index', axis=1)
df_omnibus10 = df3.loc[df3['장르'].str.contains('옴니버스, 감성'), ].reset_index().drop('index', axis=1)
## 옴니버스

## 에피소드
df_episode1 = df3.loc[df3['장르'].str.contains('에피소드, 로맨스'), ].reset_index().drop('index', axis=1)
df_episode2 = df3.loc[df3['장르'].str.contains('에피소드, 판타지'), ].reset_index().drop('index', axis=1)
df_episode3 = df3.loc[df3['장르'].str.contains('에피소드, 스포츠'), ].reset_index().drop('index', axis=1)
df_episode4 = df3.loc[df3['장르'].str.contains('에피소드, 개그'), ].reset_index().drop('index', axis=1)
df_episode5 = df3.loc[df3['장르'].str.contains('에피소드, 스릴러'), ].reset_index().drop('index', axis=1)
df_episode6 = df3.loc[df3['장르'].str.contains('에피소드, 드라마'), ].reset_index().drop('index', axis=1)
df_episode7 = df3.loc[df3['장르'].str.contains('에피소드, 액션'), ].reset_index().drop('index', axis=1)
df_episode8 = df3.loc[df3['장르'].str.contains('에피소드, 일상'), ].reset_index().drop('index', axis=1)
df_episode9 = df3.loc[df3['장르'].str.contains('에피소드, 무협/사극'), ].reset_index().drop('index', axis=1)
df_episode10 = df3.loc[df3['장르'].str.contains('에피소드, 감성'), ].reset_index().drop('index', axis=1)
## 에피소드
st.subheader('22.06.14까지의 데이터입니다.')
def main() :
    menu = ['네이버 웹툰 검색','믿고 보는 드라마 원작!','웹툰 분석']
    choice1 = st.sidebar.selectbox('메뉴' , menu)
    
    

    
    
    
    
    
    

    
        
    if choice1 == '네이버 웹툰 검색' :
        st.title('네이버 웹툰 검색 앱')
        st.image(img_url,use_column_width=True)
        with st.expander('전체 웹툰 중 별점 Top 10') :
                st.dataframe(df4.head(10).reset_index().sort_values(by='별점',ascending=False))
        
        genre1 = st.selectbox('웹툰 형식을 선택하세요. (별점 상위 50 작품)',['선택안함','스토리','옴니버스','에피소드'])
        genre2 = st.selectbox('장르를 선택하세요.',['선택안함','로맨스','판타지','스포츠','개그','스릴러','드라마','액션','일상','무협/사극','감성',])
       
        
        


    
        
        ## 스토리 if
        if genre1 == '선택안함' and genre2 =='선택안함' :
                st.warning('웹툰형식과 장르를 선택해주세요.')
        elif genre1 == '선택안함' :
                st.warning('웹툰 형식을 선택해주세요.')
        elif genre2 == '선택안함' :
                st.warning('장르를 선택해주세요')
        
        if genre1 == '스토리' and genre2 == '로맨스':
                st.dataframe(df_story1.head(51))
        if genre1 == '스토리' and genre2 == '판타지':
                st.dataframe(df_story2.head(51))
        if genre1 == '스토리' and genre2 == '스포츠':
                st.dataframe(df_story3.head(51))
        if genre1 == '스토리' and genre2 == '개그':
                st.dataframe(df_story4.head(51))
        if genre1 == '스토리' and genre2 == '스릴러':
                st.dataframe(df_story5.head(51))
        if genre1 == '스토리' and genre2 == '드라마':
                st.dataframe(df_story6.head(51))
        if genre1 == '스토리' and genre2 == '액션':
                st.dataframe(df_story7.head(51))
        if genre1 == '스토리' and genre2 == '일상':
                st.dataframe(df_story8.head(51))
        if genre1 == '스토리' and genre2 == '무협/사극':
                st.dataframe(df_story9.head(51))
        if genre1 == '스토리' and genre2 == '감성':
                st.dataframe(df_story10.head(51))
        
        

        ## 옴니버스 if
        if genre1 == '옴니버스' and genre2 == '로맨스':
                st.dataframe(df_omnibus1.head(51))
        if genre1 == '옴니버스' and genre2 == '판타지':
                st.dataframe(df_omnibus2.head(51))
        if genre1 == '옴니버스' and genre2 == '스포츠':
                st.dataframe(df_omnibus3.head(51))
        if genre1 == '옴니버스' and genre2 == '개그':
                st.dataframe(df_omnibus4.head(51))
        if genre1 == '옴니버스' and genre2 == '스릴러':
                st.dataframe(df_omnibus5.head(51))
        if genre1 == '옴니버스' and genre2 == '드라마':
                st.dataframe(df_omnibus6.head(51))
        if genre1 == '옴니버스' and genre2 == '액션':
                st.dataframe(df_omnibus7.head(51))
        if genre1 == '옴니버스' and genre2 == '일상':
                st.dataframe(df_omnibus8.head(51))
        if genre1 == '옴니버스' and genre2 == '무협/사극':
                st.dataframe(df_omnibus9.head(51))
        if genre1 == '옴니버스' and genre2 == '감성':
                st.dataframe(df_omnibus10.head(51))

        
        ## 에피소드 if
        if genre1 == '에피소드' and genre2 == '로맨스':
                st.dataframe(df_episode1.head(51))
        if genre1 == '에피소드' and genre2 == '판타지':
                st.dataframe(df_episode2.head(51))
        if genre1 == '에피소드' and genre2 == '스포츠':
                st.dataframe(df_episode3.head(51))
        if genre1 == '에피소드' and genre2 == '개그':
                st.dataframe(df_episode4.head(51))
        if genre1 == '에피소드' and genre2 == '스릴러':
                st.dataframe(df_episode5.head(51))
        if genre1 == '에피소드' and genre2 == '드라마':
                st.dataframe(df_episode6.head(51))
        if genre1 == '에피소드' and genre2 == '액션':
                st.dataframe(df_episode7.head(51))
        if genre1 == '에피소드' and genre2 == '일상':
                st.dataframe(df_episode8.head(51))
        if genre1 == '에피소드' and genre2 == '무협/사극':
                st.dataframe(df_episode9.head(51))
        if genre1 == '에피소드' and genre2 == '감성':
                st.dataframe(df_episode10.head(51))

        name = st.text_input('검색어를 입력해주세요.')

        ## Radio button
        status = st.radio("검색 필터", ("작가 이름으로 검색", "작품 제목으로 검색",'줄거리로 검색'))
        if status == "작가 이름으로 검색" and name != '' :
                st.dataframe(df3.loc[df3['작가'].str.contains(name).sort_values(ascending=False)])
        elif status =='작품 제목으로 검색' and name != '' :
                st.dataframe(df3.loc[df3['제목'].str.contains(name)])
        elif status =='줄거리로 검색' and name != '' :
                st.dataframe(df3.loc[df3['줄거리'].str.contains(name)])

       
    
        



    elif choice1 == '믿고 보는 드라마 원작!' :
        run_drama_app()
    
    elif choice1 == '웹툰 분석' :
        run_eda_app()

    


if __name__ =='__main__' :
    main()

# 데이터 출처 : https://www.kaggle.com/datasets/bmofinnjake/naverwebtoon-datakorean

