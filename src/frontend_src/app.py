from config.frontend_settings import Settings
import requests
import streamlit as st

settings = Settings()

st.set_page_config(
    page_title="AgriProof AI",
    page_icon="🌱",
    layout="centered"
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.markdown("## 🌱 AgriProof AI")
    st.caption("Evidence-Grounded Agricultural Knowledge Assistant")

    if st.button("🧹 Clear conversation", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

    st.divider()
    st.markdown("### Tips")
    st.write("- Ask about irrigation, watering, crop management, etc.")
    st.write("- Questions are answered only from agricultural documents")
    st.write("- Evidence snippets show the exact text used from sources")

st.title("🌱 AgriProof AI")
st.caption("Evidence-Grounded Agricultural Knowledge Assistant")

st.divider()

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant" and message.get("summary"):
            st.markdown("### ✅ Summary")
            st.write(message.get("summary"))
        else:
            st.markdown(message.get("content", ""))

        if message.get("role") == "assistant":
            sources = message.get("sources", []) or []
            key_points = message.get("key_points", []) or []
            evidence = message.get("evidence", []) or []

            if key_points:
                st.markdown("### 🔎 Key points")
                for p in key_points:
                    st.write(f"- {p}")

            if sources:
                st.markdown("### 📌 Sources")
                for s in sources:
                    st.write(f"- {s}")

            if evidence:
                with st.expander("🔍 View evidence snippets"):
                    for ev in evidence:
                        st.markdown(f"**{ev.get('source', '')}**")
                        st.write(ev.get("snippet") or ev.get("text") or "")
                        st.divider()


user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append(
        {"role": "user", "content": user_prompt})

    # prepare payload for API
    payload = {"chat_history": st.session_state.chat_history}
    try:
        response = requests.post(settings.CHAT_ENDPOINT_URL, json=payload)
        response.raise_for_status()
        response_json = response.json()
        summary = response_json.get("summary")
        key_points = response_json.get("key_points", [])
        sources = response_json.get("sources", [])
        evidence = response_json.get("evidence", [])

        assistant_response = response_json.get(
            "answer") or summary or "No response"

    except Exception as e:
        assistant_response = f"Error: {e}"
        summary = None
        key_points = []
        sources = []
        evidence = []

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": assistant_response,
        "summary": summary,
        "key_points": key_points,
        "sources": sources,
        "evidence": evidence,
    })

    with st.chat_message("assistant"):
        if summary:
            st.markdown("### ✅ Summary")
            st.write(summary)
        else:
            st.markdown(assistant_response)

        if key_points:
            st.markdown("### 🔎 Key points")
            for p in key_points:
                st.write(f"- {p}")

        if sources:
            st.markdown("### 📌 Sources")
            for s in sources:
                st.write(f"- {s}")

        if evidence:
            with st.expander("🔍 View evidence snippets"):
                for ev in evidence:
                    st.markdown(f"**{ev.get('source', '')}**")
                    st.write(ev.get("snippet") or ev.get("text") or "")
                    st.divider()
