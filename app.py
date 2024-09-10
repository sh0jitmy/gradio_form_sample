import gradio as gr

# カスタムCSSを適用する
css = """
.form-class {
    @apply bg-gray-100 p-6 rounded-lg shadow-md;
}

.input-class {
    @apply block w-full p-3 border border-gray-300 rounded-lg focus:ring focus:ring-blue-500;
}

.button-class {
    @apply bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600;
}
"""

def submit(name, age):
    return f"名前: {name}, 年齢: {age}"

# Gradioのインターフェース作成
with gr.Blocks(css=css) as demo:
    with gr.Column(elem_classes=["form-class"]):
        name = gr.Textbox(label="名前", placeholder="名前を入力", elem_classes=["input-class"])
        age = gr.Textbox(label="年齢", placeholder="年齢を入力", elem_classes=["input-class"])
        submit_btn = gr.Button("送信", elem_classes=["button-class"])
        output = gr.Textbox(label="結果")

        submit_btn.click(submit, inputs=[name, age], outputs=output)

# アプリを起動
demo.launch(share=True)
