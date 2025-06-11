# my-streamlit-todo-appimport streamlit as st 
def main():
    # アプリのタイトル
    st.title("シンプルなToDoリストアプリ")
    st.write("今日のやることを記録しよう！")

    # ToDoリストを保存するための場所（セッションステート）
    # アプリを閉じても内容を覚えておくための魔法の箱だよ
    if 'todos' not in st.session_state:
        st.session_state.todos = [] # 最初は空っぽのリストにする

    # --- 新しいToDoを追加する部分 ---
    st.header("新しいToDoを追加")
    new_todo = st.text_input("ここに新しいToDoを入力してください:")

    # 「追加」ボタンが押されたら
    if st.button("ToDoを追加"):
        if new_todo: # 何か文字が入力されていたら（空っぽでなければ）
            # リストに新しいToDoを追加する
            # "task"にToDoの内容、"completed"に完了したかどうか（最初はFalse=未完了）
            st.session_state.todos.append({"task": new_todo, "completed": False})
            st.success("新しいToDoが追加されました！")
            st.rerun() # 画面を更新して、追加されたToDoを表示する

    # --- 現在のToDoリストを表示する部分 ---
    st.header("現在のToDoリスト")

    if not st.session_state.todos: # ToDoが一つもなければ
        st.info("まだToDoがありません。上に入力して追加してくださいね！")
    else: # ToDoがあれば、一つずつ表示する
        # ToDoを新しい順に表示するために、リストを逆順にする
        for i, todo in enumerate(reversed(st.session_state.todos)):
            # 元のリストの正しいインデックスを取得
            original_index = len(st.session_state.todos) - 1 - i

            # 各ToDoを横に並べて表示するために、3つの列に分ける
            col1, col2, col3 = st.columns([0.6, 0.2, 0.2]) # ToDoの内容、完了状態、削除ボタンの幅

            with col1:
                # 完了チェックボックス
                # key=f"checkbox_{original_index}" は、それぞれのチェックボックスを区別するためのおまじない
                completed = st.checkbox(todo["task"], todo["completed"], key=f"checkbox_{original_index}")

                # もしチェックボックスの状態が変わったら、ToDoの完了状態を更新する
                if completed != todo["completed"]:
                    st.session_state.todos[original_index]["completed"] = completed
                    st.rerun() # 画面を更新して、状態の変更を反映させる

            with col2:
                # 完了状態のテキスト表示
                if todo["completed"]:
                    st.success("完了！")
                else:
                    st.warning("未完了")

            with col3:
                # 削除ボタン
                # key=f"delete_{original_index}" は、それぞれの削除ボタンを区別するためのおまじない
                if st.button("削除", key=f"delete_{original_index}"):
                    # そのToDoをリストから削除する
                    del st.session_state.todos[original_index]
                    st.error("ToDoが削除されました。")
                    st.rerun() # 画面を更新して、削除されたToDoを消す

# このファイルが直接実行されたら、main関数を呼び出す
if __name__ == "__main__":
    main()
