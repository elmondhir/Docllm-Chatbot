import streamlit as st
import ollama

# Initialize history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Initialize model
if "model" not in st.session_state:
    st.session_state["model"] = ""

# Select the model
models = [model["model"] for model in ollama.list()["models"]]
st.session_state["model"] = st.selectbox("Choose your model", models)

def model_res_generator(user_prompt):
    prompt = """If you are a doctor, please answer the medical questions based on the patient's description:
    Input: {input}
    Output: {output}
    """
    formatted_prompt = prompt.format(input=user_prompt, output="")  # Leave output blank for generation

    # Replace user input with formatted prompt
    messages = [{"role": "user", "content": formatted_prompt}]
    stream = ollama.chat(
        model=st.session_state["model"],
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        yield chunk["message"]["content"]

# Display chat messages from history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input for user interaction
if prompt := st.chat_input("What is up?"):
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message = st.write_stream(model_res_generator(prompt))
        st.session_state["messages"].append({"role": "assistant", "content": message})
