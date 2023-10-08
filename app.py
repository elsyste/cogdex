import streamlit as st
from streamlit.components.v1 import html


# 공유된 구글 슬라이드의 링크
slide_url = "https://docs.google.com/presentation/d/e/2PACX-1vR0kPLGtR_nxqoB1srjsSxuSSyPcMt3T8fWuVJJF4FVNi6xk_7u36xRy_XHaZMPQq9iad_ZooFwvFUa/embed?start=false&loop=false&delayms=3000"
google_slide_direct_link = "https://docs.google.com/presentation/d/1xzdkFx6__bZ-acvcjaeGY5GbCzBs0dqFvGIC8QTDRRM/edit?usp=sharing"  



# Streamlit 앱에 제목 추가
st.header("디코더 유형 트랜스포머 아키텍처 개론")
st.subheader("GPT의 동작 원리가 궁금하신가요?")
st.write("GPT와 같은 디코더 유형 트랜스포머 아키텍처에 대한 개념 위주의 튜토리얼을 제공합니다")

# # 부모 컨테이너의 최소 높이 설정
# st.markdown(
#     """
#     <div style="position: relative; width: 960px; min-height: 639px;"> <!-- 배너의 높이(70px)를 추가한 높이로 설정 -->
#         <iframe src="{slide_url}" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
#         <iframe width="220" style="position: absolute; bottom: 0; right: 10px;">
#             <!-- 배너 내용 -->
#         </iframe>
#     </div>
#     """.format(slide_url=slide_url),
#     unsafe_allow_html=True,
# )

# 부모 컨테이너의 최소 높이 설정
st.markdown(
    """
    <div style="position: relative; width: 960px; min-height: 669px;"> <!-- 배너의 높이(100px)를 추가한 높이로 설정 -->
        <iframe src="{slide_url}" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
        <iframe width="220" style="position: absolute; bottom: 0; right: 10px;">
            <!-- 배너 내용 -->
        </iframe>
    </div>
    """.format(slide_url=slide_url),
    unsafe_allow_html=True,
)


# 미디어 쿼리를 사용하여 화면 높이에 따라 스타일 적용
# st.markdown(
#     """
#     <style>
#         @media (max-height: 700px) {
#             iframe[width="220"] {
#                 position: static; /* 배너의 위치를 기본 값으로 설정 */
#                 display: block;
#                 margin: 10px auto; /* 중앙 정렬 */
#             }
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )



# # 슬라이드 임베드(상대 위치 사용)
# st.markdown(
#     """
#     <div style="position: relative; width: 960px; height: 639px;"> <!-- 배너의 높이(70px)를 추가한 높이로 설정 -->
#         <iframe src="{slide_url}" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
#         <iframe width="220" style="position: absolute; bottom: 0; right: 10px;">
#             <!-- 배너 내용 -->
#         </iframe>
#     </div>
#     """.format(slide_url=slide_url),
#     unsafe_allow_html=True,
# )

# 슬라이드를 임베드합니다..
# st.markdown(f'<iframe src="{slide_url}" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>', unsafe_allow_html=True)

#바이미어커피 예전
# button = """
# <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="rdjhyoonc" data-color="#FFDD00" data-emoji="☕"  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
# """

#바이미어커피 수정
button = """
<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="rdjhyoonc" data-color="#FFDD00" data-emoji="☕"  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
"""

html(button, height=70, width=220)

st.markdown(button, unsafe_allow_html=True)

# st.markdown(
#     """
#     <style>
#         iframe[width="220"] {
#             position: fixed;
#             bottom: 100px;
#             right: 350px;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )


#st.write("Write Something")
#st.markdown(f"여기에는 어떤 것이 들어오면 좋을까요?", unsafe_allow_html=True)

# 사용자에게 전체 화면으로 보기를 권장하는 메시지와 링크 제공
#st.markdown(f"전체 화면으로 슬라이드쇼를 보려면 [여기]( {google_slide_direct_link} )를 클릭하세요.", unsafe_allow_html=True)