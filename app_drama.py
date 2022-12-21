import pandas as pd
import streamlit as st
from PIL import Image
url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjkw&x_csa=%7B%22pkid%22%3A%2257%22%2C%20%22isOpen%22%3Afalse%2C%20%22tab%22%3A%22default_info%22%7D&pkid=57&os=2217221&qvt=0&query=%EC%B9%98%EC%A6%88%EC%9D%B8%EB%8D%94%ED%8A%B8%EB%9E%A9%20%EC%A0%95%EB%B3%B4'
df = pd.read_csv('naver.csv')
print(df)
df.rename(columns = {'title' : '제목'}, inplace = True)
df.rename(columns = {'author' : '작가'}, inplace = True)
df.rename(columns = {'genre' : '장르'}, inplace = True)
df.rename(columns = {'description' : '줄거리'}, inplace = True)
df.rename(columns = {'age' : '연령'}, inplace = True)
df.rename(columns = {'completed' : '완결 여부'}, inplace = True)
df.rename(columns = {'free' : '무료 여부'}, inplace = True)
df.rename(columns = {'rating' : '별점'}, inplace = True)
df2 = df.loc[ : ,['제목','작가','장르','별점','연령','줄거리']   ]
df3 = df2.sort_values(by='별점',ascending=False)
# 치인트
url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjkw&x_csa=%7B%22pkid%22%3A%2257%22%2C%20%22isOpen%22%3Afalse%2C%20%22tab%22%3A%22default_info%22%7D&pkid=57&os=2217221&qvt=0&query=%EC%B9%98%EC%A6%88%EC%9D%B8%EB%8D%94%ED%8A%B8%EB%9E%A9%20%EC%A0%95%EB%B3%B4'
img = Image.open('cit.PNG')
img2 = Image.open('cit2.PNG')


#쌉니다 천리마
url2 = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjkw&x_csa=%7B%22pkid%22%3A%2257%22%2C%20%22isOpen%22%3Afalse%2C%20%22tab%22%3A%22default_info%22%7D&pkid=57&os=9504329&qvt=0&query=%EC%8C%89%EB%8B%88%EB%8B%A4%20%EC%B2%9C%EB%A6%AC%EB%A7%88%EB%A7%88%ED%8A%B8%20%EC%A0%95%EB%B3%B4'
img3 = Image.open('3.PNG')
img4 = Image.open('4.PNG')

#알고있지만
url3 = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjkw&x_csa=%7B%22pkid%22%3A%2257%22%2C%20%22isOpen%22%3Afalse%2C%20%22tab%22%3A%22default_info%22%7D&pkid=57&os=18089981&qvt=0&query=%EC%95%8C%EA%B3%A0%EC%9E%88%EC%A7%80%EB%A7%8C%20%EC%A0%95%EB%B3%B4'
img5 = Image.open('5.PNG')
img6 = Image.open('6.PNG')

#간 떨 동
url4 = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjkw&x_csa=%7B%22pkid%22%3A%2257%22%2C%20%22isOpen%22%3Afalse%2C%20%22tab%22%3A%22default_info%22%7D&pkid=57&os=17534068&qvt=0&query=%EA%B0%84%20%EB%96%A8%EC%96%B4%EC%A7%80%EB%8A%94%20%EB%8F%99%EA%B1%B0%20%EC%A0%95%EB%B3%B4'
img7 = Image.open('7.PNG')
img8 = Image.open('8.PNG')

# 스위트홈
url5 = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blFB&x_csa=%7B%22tab%22%3A%22info%22%2C%22pkid%22%3A%22356%22%7D&pkid=356&os=16962417&qvt=0&query=%EC%8A%A4%EC%9C%84%ED%8A%B8%ED%99%88%20%EC%8B%9C%EC%A6%8C1'
img9 = Image.open('9.PNG')
# img10 = Image.open('10.PNG')

# 유미의 세포들
url6 = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blFB&x_csa=%7B%22tab%22%3A%22info%22%2C%22pkid%22%3A%22356%22%7D&pkid=356&os=26126877&qvt=0&query=%EC%9C%A0%EB%AF%B8%EC%9D%98%20%EC%84%B8%ED%8F%AC%EB%93%A4%20%EC%8B%9C%EC%A6%8C2'
img11 = Image.open('11.PNG')
# img12 = Image.open('12.PNG')

# 한번 더 해요
url7 = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjkw&x_csa=%7B%22pkid%22%3A%2257%22%2C%20%22isOpen%22%3Afalse%2C%20%22tab%22%3A%22default_info%22%7D&pkid=57&os=6205149&qvt=0&query=%EA%B3%A0%EB%B0%B1%EB%B6%80%EB%B6%80%20%EC%A0%95%EB%B3%B4'
img13 = Image.open('13.PNG')
img14 = Image.open('14.PNG')

# 모범 택시
url8 = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjkw&x_csa=%7B%22pkid%22%3A%2257%22%2C%20%22isOpen%22%3Afalse%2C%20%22tab%22%3A%22default_info%22%7D&pkid=57&os=26500634&qvt=0&query=%EB%AA%A8%EB%B2%94%ED%83%9D%EC%8B%9C2%20%EC%A0%95%EB%B3%B4'
img15 = Image.open('15.PNG')
img16 = Image.open('16.PNG')

# 지옥
url9 = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blFB&x_csa=%7B%22tab%22%3A%22info%22%2C%22pkid%22%3A%22356%22%7D&pkid=356&os=17491380&qvt=0&query=%EC%A7%80%EC%98%A5'
img17 = Image.open('17.PNG')
#img18 = Image.open('18.PNG')

# 내 ID
url10 = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjkw&x_csa=%7B%22pkid%22%3A%2257%22%2C%20%22isOpen%22%3Afalse%2C%20%22tab%22%3A%22default_info%22%7D&pkid=57&os=8259620&qvt=0&query=%EB%82%B4%20%EC%95%84%EC%9D%B4%EB%94%94%EB%8A%94%20%EA%B0%95%EB%82%A8%EB%AF%B8%EC%9D%B8%20%EC%A0%95%EB%B3%B4'
img19 = Image.open('19.PNG')
img20 = Image.open('20.PNG')

# 지금 우리 학교는
url11 = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blFB&x_csa=%7B%22tab%22%3A%22info%22%2C%22pkid%22%3A%22356%22%7D&pkid=356&os=17491372&qvt=0&query=%EC%A7%80%EA%B8%88%20%EC%9A%B0%EB%A6%AC%20%ED%95%99%EA%B5%90%EB%8A%94%20%EC%8B%9C%EC%A6%8C1'
img21 = Image.open('21.PNG')
#img22 = Image.open('22.PNG')


img_url = 'https://mblogthumb-phinf.pstatic.net/MjAxODAyMTJfMjEg/MDAxNTE4NDA5MTUyNTkx._YP_LlMbDs_l2HE-JuUIk-MocIto8dNU_gjSdaBHWJUg.ZeMhXrK6KAfLAtZWZ0Xtolcpq3AQsMII7cWrq5Pu5Log.JPEG.hanarokson/%EC%9B%B9%ED%88%B0%EC%9B%90%EC%9E%91%EB%93%9C%EB%9D%BC%EB%A7%88.jpg?type=w800'









def run_drama_app() :
    st.title('웹툰 원작 드라마 정보')
    st.image(img_url,width=500)

    st.dataframe(df3.loc[df3['제목'].str.contains('드라마') , ].sort_values(by='별점' ,ascending=False))
    
    
    choice_drama = st.selectbox('정보를 볼 드라마 제목을 선택하세요.',['치즈인더트랩','쌉니다 천리마 마트','알고있지만','간 떨어지는 동거','스위트홈','유미의 세포들','한번 더 해요','모범 택시','지옥','내 ID는 강남미인','지금 우리 학교는'])
    #차
    if choice_drama == '치즈인더트랩' :
        with st.expander('정보 바로가기') :
            st.markdown(f'''<a href={url}><button style="background-color:GreenYellow;">Stackoverflow</button></a>''',unsafe_allow_html=True)
        with st.expander('등장인물, 시청률') :
            st.image([img,img2],use_column_width=True)
        
        
    elif choice_drama == '쌉니다 천리마 마트' :
        with st.expander('정보 바로가기') :
            st.markdown(f'''<a href={url2}><button style="background-color:GreenYellow;">Stackoverflow</button></a>''',unsafe_allow_html=True)
        with st.expander('등장인물, 시청률') :
            st.image([img3,img4],use_column_width=True)
    
    elif choice_drama == '알고있지만' :
        with st.expander('정보 바로가기') :
            st.markdown(f'''<a href={url3}><button style="background-color:GreenYellow;">Stackoverflow</button></a>''',unsafe_allow_html=True)
        with st.expander('등장인물, 시청률') :
            st.image([img5,img6],use_column_width=True)

    elif choice_drama == '간 떨어지는 동거' :
        with st.expander('정보 바로가기') :
            st.markdown(f'''<a href={url4}><button style="background-color:GreenYellow;">Stackoverflow</button></a>''',unsafe_allow_html=True)
        with st.expander('등장인물, 시청률') :
            st.image([img7,img8],use_column_width=True)
    
    elif choice_drama == '스위트홈' :
        with st.expander('정보 바로가기') :
            st.markdown(f'''<a href={url5}><button style="background-color:GreenYellow;">Stackoverflow</button></a>''',unsafe_allow_html=True)
        with st.expander('등장인물, 시청률') :
            st.image(img9,use_column_width=True)

    elif choice_drama == '유미의 세포들' :
        with st.expander('정보 바로가기') :
            st.markdown(f'''<a href={url6}><button style="background-color:GreenYellow;">Stackoverflow</button></a>''',unsafe_allow_html=True)
        with st.expander('등장인물, 시청률') :
            st.image(img11,use_column_width=True)
        
    elif choice_drama == '한번 더 해요' :
        st.text('이 작품은 드라마화 과정에서 제목이 [고백부부]로 변경되었습니다.')
        with st.expander('정보 바로가기') :
            st.markdown(f'''<a href={url7}><button style="background-color:GreenYellow;">Stackoverflow</button></a>''',unsafe_allow_html=True)
        with st.expander('등장인물, 시청률') :
            st.image([img13,img14],use_column_width=True)
        
    elif choice_drama == '모범 택시' :
        with st.expander('정보 바로가기') :
            st.markdown(f'''<a href={url8}><button style="background-color:GreenYellow;">Stackoverflow</button></a>''',unsafe_allow_html=True)
        with st.expander('등장인물, 시청률') :
            st.image([img15,img16],use_column_width=True)
    
    elif choice_drama == '지옥' :
        with st.expander('정보 바로가기') :
            st.markdown(f'''<a href={url9}><button style="background-color:GreenYellow;">Stackoverflow</button></a>''',unsafe_allow_html=True)
        with st.expander('등장인물, 시청률') :
            st.image(img17,use_column_width=True)
    
    elif choice_drama == '내 ID는 강남미인' :
        with st.expander('정보 바로가기') :
            st.markdown(f'''<a href={url10}><button style="background-color:GreenYellow;">Stackoverflow</button></a>''',unsafe_allow_html=True)
        with st.expander('등장인물, 시청률') :
            st.image([img19,img20],use_column_width=True)

    elif choice_drama == '지금 우리 학교는' :
        with st.expander('정보 바로가기') :
            st.markdown(f'''<a href={url11}><button style="background-color:GreenYellow;">Stackoverflow</button></a>''',unsafe_allow_html=True)
        with st.expander('등장인물') :
            st.image(img21,use_column_width=True)

        
    
        

    
    




    