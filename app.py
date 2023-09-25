import streamlit as st

# 공유된 구글 슬라이드의 링크
slide_url = "https://docs.google.com/presentation/d/1xzdkFx6__bZ-acvcjaeGY5GbCzBs0dqFvGIC8QTDRRM/edit?usp=sharing"

# Streamlit 앱에 제목 추가
st.title('GPT 동작 원리 개론')


# 슬라이드를 임베드합니다.
st.markdown(f'<iframe src="{slide_url}" width="700" height="400"></iframe>', unsafe_allow_html=True)


