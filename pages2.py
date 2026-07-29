import streamlit as st

st.set_page_config(page_title="상담가 쌤의 시크릿 추천", page_icon="📚")

st.title("📚 상담가 쌤의 시크릿 추천!")
st.markdown("진로 탐색만큼 중요한 건 나에게 딱 맞는 **공부법과 활동**을 찾는 거예요! 쌤이 성향에 맞춰 준비해 봤어. 😉")

st.divider()

study_tips = {
    "E (외향형)": "친구들과 묻고 답하는 스터디 그룹이 최고! 🗣️",
    "I (내향형)": "조용하고 익숙한 공간에서 혼자 딥하게 집중할 때 능률 쑥쑥! 🎧",
    "S (감각형)": "교과서, 기출문제 위주로 꼼꼼하게 암기하기! 📖",
    "N (직관형)": "마인드맵으로 숲을 먼저 보고 전체적인 흐름 파악하기! 🌳",
    "T (사고형)": "원리와 인과관계를 철저히 분석하고 논리적으로 이해하기! 🔍",
    "F (감정형)": "스토리를 만들어 외우거나 좋아하는 선생님 과목 파고들기! 💖",
    "J (판단형)": "플래너는 나의 무기! 시간별로 체계적인 계획 세우기 📅",
    "P (인식형)": "융통성 있게 그때그때 꽂히는 과목 몰입해서 끝내기! ⚡"
}

st.subheader("🔍 나의 성향에 맞는 공부법 조립하기")
with st.expander("에너지 방향: E vs I"):
    st.write(f"- **E 유형:** {study_tips['E (외향형)']}")
    st.write(f"- **I 유형:** {study_tips['I (내향형)']}")

with st.expander("정보 수집: S vs N"):
    st.write(f"- **S 유형:** {study_tips['S (감각형)']}")
    st.write(f"- **N 유형:** {study_tips['N (직관형)']}")

with st.expander("결정 방식: T vs F"):
    st.write(f"- **T 유형:** {study_tips['T (사고형)']}")
    st.write(f"- **F 유형:** {study_tips['F (감정형)']}")

with st.expander("생활 양식: J vs P"):
    st.write(f"- **J 유형:** {study_tips['J (판단형)']}")
    st.write(f"- **P 유형:** {study_tips['P (인식형)']}")

st.divider()

st.subheader("🎸 성향별 추천 동아리 활동")
activity = st.selectbox("학교에서 어떤 계열에 관심이 있니?", ["선택해줘!", "문과/예체능 성향 (F, N 뿜뿜)", "이과/분석 성향 (T, S 뿜뿜)", "리더십/활동 성향 (E, J 뿜뿜)"])

if activity == "문과/예체능 성향 (F, N 뿜뿜)":
    st.success("방송부 🎥, 또래 상담부 👂, 교지 편집부 ✍️, 연극부 🎭를 추천해!")
elif activity == "이과/분석 성향 (T, S 뿜뿜)":
    st.info("과학 탐구 실험부 🔬, 코딩/로봇 동아리 💻, 경제 수학부 📈가 딱이야!")
elif activity == "리더십/활동 성향 (E, J 뿜뿜)":
    st.warning("학생회 활동 🙋, 모의유엔(MUN) 🌍, 토론부 🗣️, 스포츠 클럽 🏀 어때?")