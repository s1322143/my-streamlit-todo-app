import streamlit as st
import datetime


def main():
    st.set_page_config(layout="centered")

    st.title("🌈 気分で選ぶ！絵文字ToDoリスト ✨")
    st.write("今日の気分を選んで、ToDoを絵文字で彩ろう！")

    if 'todos' not in st.session_state:
        st.session_state.todos = []

    st.subheader("📝 新しいToDoを追加")

    new_task = st.text_input("やることリスト（例: 買い物に行く）", key="new_task_input")

    emoji_options = ["✨", "💡", "💖", "🚀", "🌱", "📚", "🎨", "🎵", "💪", "🌈", "📝"]
    selected_emoji = st.selectbox("このToDoに合う絵文字を選んでね", emoji_options, key="emoji_select")

    st.subheader("今日の気分はどう？")
    mood_options = ["😞 最悪", "🙁 いまいち", "😐 普通", "🙂 良い", "😃 最高！"]
    selected_mood_index = st.slider("スライドして選んでね", 0, len(mood_options) - 1, 2)
    current_mood = mood_options[selected_mood_index]
    st.write(f"今の気分は：**{current_mood}**")


    if st.button("➕ ToDoに追加！", key="add_todo_button"):
        if new_task:
            st.session_state.todos.append({
                "task": new_task,
                "completed": False,
                "emoji": selected_emoji,
                "mood_at_creation": current_mood
            })
            st.success("新しいToDoが追加されました！")
            st.rerun()
        else:
            st.warning("ToDoの内容を入力してください！")

    st.markdown("---")
    st.subheader("✅ あなたのToDoリスト")

    if not st.session_state.todos:
        st.info("まだToDoがありません。上に追加して、絵文字で飾ってみよう！")
    else:
        st.write("---")
        for i, todo in enumerate(reversed(st.session_state.todos)):
            original_index = len(st.session_state.todos) - 1 - i

            col_checkbox, col_task_info, col_delete = st.columns([0.1, 0.7, 0.2])

            with col_checkbox:
                completed = st.checkbox("", todo["completed"], key=f"emoji_checkbox_{original_index}")
                if completed != todo["completed"]:
                    st.session_state.todos[original_index]["completed"] = completed
                    st.rerun()

            with col_task_info:
                display_text = f"{todo['emoji']} {todo['task']}"
                if todo["completed"]:
                    st.markdown(f"<span style='color:green;'><del>{display_text}</del></span>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<span style='color:blue;'>{display_text}</span>", unsafe_allow_html=True)
                
                st.markdown(f"<small>追加時の気分: {todo['mood_at_creation']}</small>", unsafe_allow_html=True)

            with col_delete:
                if st.button("消す", key=f"emoji_delete_{original_index}"):
                    del st.session_state.todos[original_index]
                    st.error("ToDoを削除しました。")
                    st.rerun()
            st.markdown("---")

if __name__ == "__main__":
    main()
