import streamlit as st

api_key = st.secrets.get("OPENAI_API_KEY", None)

if not api_key:
    st.error("❌ OpenAI API 키가 설정되지 않았습니다! `.streamlit/secrets.toml` 파일을 확인하세요.")
else:
    st.success("✅ API 키가 정상적으로 로드되었습니다.")
