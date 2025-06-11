# my-streamlit-todo-app
import streamlit as st 

def main():
    # アプリのタイトル
    st.title("シンプルなToDoリストアプリ")
    st.write("今日のやることを記録しよう！")

    if 'todos' not in st.session_state:
        st.session_state.todos = [] 
        
    st.header("新しいToDoを追加")
    new_todo = st.text_input("ここに新しいToDoを入力してください:")

    if st.button("ToDoを追加"):
        if new_todo 
            # "task"にToDoの内容、"completed"に完了したかどうか（最初はFalse=未完了）
            st.session_state.todos.append({"task": new_todo, "completed": False})
            st.success("新しいToDoが追加されました！")
            st.rerun() 

    st.header("現在のToDoリスト")

    if not st.session_state.todos:
        st.info("まだToDoがありません。上に入力して追加してくださいね！")
    else: 
        for i, todo in enumerate(reversed(st.session_state.todos)):
            original_index = len(st.session_state.todos) - 1 - i

            col1, col2, col3 = st.columns([0.6, 0.2, 0.2]) 

            with col1:
                
                completed = st.checkbox(todo["task"], todo["completed"], key=f"checkbox_{original_index}")

                if completed != todo["completed"]:
                    st.session_state.todos[original_index]["completed"] = completed
                    st.rerun() 

            with col2:
                
                if todo["completed"]:
                    st.success("完了！")
                else:
                    st.warning("未完了")

            with col3:
                
                if st.button("削除", key=f"delete_{original_index}"):
                    del st.session_state.todos[original_index]
                    st.error("ToDoが削除されました。")
                    st.rerun() 

if __name__ == "__main__":
    main()
