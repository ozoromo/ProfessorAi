import gradio as gr




llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model=model)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())
conversational_qa_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=db.as_retriever(), memory=memory)



def answer_question(question):
    question_result = conversational_qa_chain({"question": question})
    return question_result["answer"]

QA_Interface = gr.Interface(fn=answer_question, 
    inputs="text", 
    outputs="text",
    layout="vertical"
    )

with gr.Blocks() as chat_ui:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = answer_question(message)
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

chat_ui.launch()
