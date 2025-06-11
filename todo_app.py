import streamlit as st
import datetime

def main():
    st.set_page_config(layout="wide")
    st.title("⭐️ あなただけの特別なToDoリスト 🗓️")
    st.write("やるべきことを、もっと楽しく管理しよう！")

    if 'todos' not in st.session_state:
        st.session_state.todos = []

    st.subheader("新しいToDoを追加しよう！")

    col_task, col_priority, col_due = st.columns([0.5, 0.2, 0.3])

    with col_task:
        new_task = st.text_input("やることリスト", key="new_task_input")

    with col_priority:
        priority_options = {
            "☆☆☆☆☆": 0,
            "★☆☆☆☆": 1,
            "★★☆☆☆": 2,
            "★★★☆☆": 3,
            "★★★★☆": 4,
            "★★★★★": 5
        }
        selected_priority_text = st.selectbox("重要度", list(priority_options.keys()), index=0, key="priority_select")
        new_priority = priority_options[selected_priority_text]

    with col_due:
        new_due_date = st.date_input("締め切り日 (任意)", value=None, key="due_date_input")

    if st.button("🌟 ToDoに追加", key="add_todo_button"):
        if new_task:
            due_date_str = new_due_date.strftime("%Y-%m-%d") if new_due_date else "未設定"
            st.session_state.todos.append({
                "task": new_task,
                "completed": False,
                "priority": new_priority,
                "due_date": new_due_date
            })
            st.success("新しいToDoが追加されました！") # 色付きメッセージ
            st.rerun()
        else:
            st.warning("ToDoの内容を入力してください！") # 色付きメッセージ

    st.markdown("---")
    st.subheader("🗓️ あなたのToDoリスト")

    sort_option = st.selectbox(
        "並び替え:",
        ["追加が新しい順", "重要度が高い順", "締め切りが近い順"],
        key="sort_option"
    )

    display_todos = st.session_state.todos[:]

    if sort_option == "重要度が高い順":
        display_todos.sort(key=lambda x: x["priority"], reverse=True)
    elif sort_option == "締め切りが近い順" and any(t["due_date"] is not None for t in display_todos):
        display_todos.sort(key=lambda x: x["due_date"] if x["due_date"] is not None else datetime.date.max)
    elif sort_option == "追加が新しい順":
        display_todos.reverse()

    if not display_todos:
        st.info("まだToDoがありません。上に追加して、あなたのリストを彩ろう！") # 色付きメッセージ
    else:
        st.write("---")
        for i, todo in enumerate(display_todos):
            original_index = st.session_state.todos.index(todo)

            col_done, col_item, col_status, col_actions = st.columns([0.1, 0.5, 0.2, 0.2])

            with col_done:
                completed = st.checkbox("", todo["completed"], key=f"unique_checkbox_{original_index}")
                if completed != todo["completed"]:
                    st.session_state.todos[original_index]["completed"] = completed
                    st.rerun()

            with col_item:
                task_display = todo["task"]
                if todo["completed"]:
                    # 完了したToDoの文字を緑色にして、線を入れる
                    st.markdown(f"<span style='color:green;'><del>{task_display}</del></span>", unsafe_allow_html=True)
                else:
                    # 未完了のToDoの文字を青色にする（例）
                    st.markdown(f"<span style='color:blue;'>{task_display}</span>", unsafe_allow_html=True)


                priority_stars = "★" * todo["priority"] + "☆" * (5 - todo["priority"])
                # 重要度の星の数をオレンジ色にする
                st.markdown(f"<small><span style='color:orange;'>重要度: {priority_stars}</span></small>", unsafe_allow_html=True)
                
                due_date_text = todo["due_date"].strftime("%Y年%m月%d日") if todo["due_date"] else "締め切りなし"
                # 締め切り日を灰色にする
                st.markdown(f"<small><span style='color:gray;'>締め切り: {due_date_text}</span></small>", unsafe_allow_html=True)


            with col_status:
                if todo["completed"]:
                    st.success("完了！🎉") # Streamlitの色付きメッセージ
                else:
                    if todo["due_date"] and todo["due_date"] < datetime.date.today():
                        st.error("期限切れ！😱") # Streamlitの色付きメッセージ（赤）
                    else:
                        st.warning("未完了") # Streamlitの色付きメッセージ（黄）

            with col_actions:
                if st.button("削除", key=f"unique_delete_{original_index}"):
                    del st.session_state.todos[original_index]
                    st.error("ToDoが削除されました。") # Streamlitの色付きメッセージ（赤）
                    st.rerun()
            st.markdown("---")

if __name__ == "__main__":
    main()
