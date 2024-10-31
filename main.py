import streamlit as st

# 제목에 그라데이션과 셔틀콕 이모지 추가
st.markdown(
    """
    <div style='text-align: center; display: flex; align-items: center; justify-content: center;'>
        <h1 style='
            font-family: Arial, sans-serif;
            font-weight: bold;
            background: -webkit-linear-gradient(45deg, #FF6B6B, #4CAF50);
            -webkit-background-clip: text;
            color: transparent;
            font-size: 3em;
            margin-right: 10px;
        '>
            배드민턴 기초와 기술
        </h1>
        <span style='font-size: 1.5em;'>🏸</span>
    </div>
    <p style='text-align: center; color: #555; font-size: 20px;'>
        배드민턴의 기본 정보와 기술을 학습할 수 있는 가이드입니다.<br>
        초보자부터 중급자까지 배울 수 있는 내용으로 구성되어 있습니다.
    </p>
    """, 
    unsafe_allow_html=True
)

# 사이드바에 선택 항목 추가
st.sidebar.title("항목을 PICK !")
options = [None, "배드민턴 개요", "기본 규칙", "기본 자세", "기본 기술", "연습 프로그램 제안", "배드민턴 기술 영상", "피드백"]
choice = st.sidebar.radio("항목 선택", options, index=0, format_func=lambda x: '선택해주세요' if x is None else x)

# 선택한 항목에 따른 내용 표시
if choice == "배드민턴 개요":
    st.header("배드민턴 개요")
    st.write("""
    배드민턴은 셔틀콕을 라켓으로 쳐서 상대방 코트에 떨어뜨리는 스포츠입니다.
    주요 장점으로는 민첩성과 반사 신경을 기를 수 있으며, 체력과 집중력을 요구합니다.
    """)

elif choice == "기본 규칙":
    st.header("기본 규칙")
    st.write("""
    - 경기 종류: 단식과 복식으로 나뉘며, 각각 규칙이 다릅니다.
    - 득점 방식: 셔틀콕이 상대방 코트에 떨어지면 득점합니다.
    - 서브 규칙: 셔틀콕을 허리 아래에서 쳐야 하며, 서브 위치는 득점에 따라 변경됩니다.
    """)

if choice == "기본 자세":
    st.header("기본 자세")
    stance_options = ["준비 자세 (스탠스)", "포핸드 그립", "백핸드 그립"]
    stance_choice = st.selectbox("기본 자세를 선택하세요", stance_options)

    if stance_choice == "준비 자세 (스탠스)":
        st.write("양 발을 어깨 너비로 벌리고 무릎을 약간 구부려서 낮은 자세를 유지합니다. 준비 자세는 빠르게 반응할 수 있도록 도와줍니다.")
        st.image("images/스탠스 자세.jpg", caption="준비 자세 (스탠스)", use_column_width=True)  # 로컬 이미지

    elif stance_choice == "포핸드 그립":
        st.write("라켓을 편안하게 잡고 손목을 자유롭게 움직일 수 있도록 합니다. 일반적으로 라켓을 자연스럽게 잡아 엄지와 검지로 고정합니다.")
        st.image("images/포핸드 그립.jpg", caption="포핸드 그립", use_column_width=True)  # 로컬 이미지

    elif stance_choice == "백핸드 그립":
        st.write("반대편에서 오는 셔틀콕을 맞출 수 있도록 손목을 돌려 라켓을 잡습니다.")
        st.image("images/백핸드 그립.jpg", caption="백핸드 그립", use_column_width=True)

elif choice == "기본 기술":
    st.header("기본 기술")
    technique_options = ["클리어", "드롭샷", "스매시"]
    technique_choice = st.selectbox("기본 기술을 선택하세요", technique_options)

    if technique_choice == "클리어":
        st.write("셔틀콕을 멀리 쳐서 상대방 코트 뒤쪽으로 보내는 기술입니다. 강하게 타격하여 상대방이 준비할 시간을 줄일 수 있습니다.")
        st.video("https://www.youtube.com/watch?v=ncIGB0oHtN8")  # 클리어 관련 YouTube 영상 링크 추가
    elif technique_choice == "드롭샷":
        st.write("셔틀콕을 네트 가까이로 가볍게 쳐서 상대방이 빠르게 반응하지 못하도록 유도하는 기술입니다.")
        st.video("https://www.youtube.com/watch?v=bgxmWqdLqBk")  # 드롭샷 관련 YouTube 영상 링크 추가
    elif technique_choice == "스매시":
        st.write("강하게 셔틀콕을 내리치는 공격적인 기술로, 상대방의 반응을 어렵게 만듭니다.")
        st.video("https://www.youtube.com/watch?v=obDRBdaag1E")  # 스매시 관련 YouTube 영상 링크 추가

elif choice == "연습 프로그램 제안":
    st.header("연습 프로그램 제안")
    level = st.selectbox("연습 수준을 선택하세요", ["초보자", "중급자", "고급자"])

    def get_training_plan(level):
        if level == "초보자":
            return ["기본 스탠스와 그립 연습", "클리어와 드롭샷 연습", "기초 풋워크"]
        elif level == "중급자":
            return ["스매시 연습", "복식 게임 연습", "고급 풋워크"]
        elif level == "고급자":
            return ["고급 스매시와 드롭샷", "전략 훈련", "반사 신경 훈련"]

    training_plan = get_training_plan(level)
    st.write("추천 훈련 계획:")
    for idx, item in enumerate(training_plan, 1):
        st.write(f"{idx}. {item}")

elif choice == "배드민턴 기술 영상":
    st.header("배드민턴 기술 학습 영상")
    st.write("아래는 주요 배드민턴 기술에 대한 설명 및 학습 영상입니다.")
    st.video("https://www.youtube.com/watch?v=--x5zNKztdY")  # YouTube 영상 URL

elif choice == "피드백":
    st.header("피드백")
    feedback = st.text_input("배드민턴 기초 가이드에 대한 피드백을 남겨주세요:")
    if feedback:
        st.write("감사합니다! 피드백이 접수되었습니다.")