import streamlit as st

st.set_page_config(page_title="나라별 MBTI 분포도", page_icon="🌍")

st.title("🌍 세계의 친구들은 어떨까?")
st.markdown("우물 안 개구리는 그만! ✈️ 다른 나라 사람들은 어떤 성격 유형을 많이 가지고 있는지 살펴볼까요?")

st.divider()

st.subheader("🗺️ 주요 국가별 가장 많은 MBTI TOP 3")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🇺🇸 미국")
    st.success("1위: **ISFJ** 👼")
    st.success("2위: **ESFJ** 🌻")
    st.success("3위: **ESTJ** 📋")

with col2:
    st.markdown("### 🇯🇵 일본")
    st.warning("1위: **INFP** 🌸")
    st.warning("2위: **ENFP** 🌈")
    st.warning("3위: **INTP** 🧠")

with col3:
    st.markdown("### 🇬🇧 영국")
    st.info("1위: **ISFJ** 👼")
    st.info("2위: **ESFJ** 🌻")
    st.info("3위: **ISTJ** 🧂")

st.divider()

st.markdown("""
💬 **상담가 쌤의 생각 넓히기:**  
나라마다 성격 유형 분포가 다르다는 게 신기하죠? 문화적인 배경이 사람들의 성향에도 영향을 미친답니다. 
우리 친구들도 세계를 무대로 멋진 꿈을 펼쳐보길 응원할게요! 🌟
""")