import streamlit as st

# 공유된 구글 슬라이드의 링크
slide_url = "https://docs.google.com/presentation/d/e/2PACX-1vR0kPLGtR_nxqoB1srjsSxuSSyPcMt3T8fWuVJJF4FVNi6xk_7u36xRy_XHaZMPQq9iad_ZooFwvFUa/embed?start=false&loop=false&delayms=3000"
google_slide_direct_link = "https://docs.google.com/presentation/d/1xzdkFx6__bZ-acvcjaeGY5GbCzBs0dqFvGIC8QTDRRM/copy?usp=sharing"  

# Streamlit 앱에 제목 추가
st.title('An overview of how GPT works')


# 슬라이드를 임베드합니다.
st.markdown(f'<iframe src="{slide_url}" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>', unsafe_allow_html=True)

# 사용자에게 전체 화면으로 보기를 권장하는 메시지와 링크 제공
st.markdown(f"전체 화면으로 슬라이드쇼를 보려면 [여기]( {google_slide_direct_link} )를 클릭하세요.", unsafe_allow_html=True)
