# **DocLLM-Chatbot**
*A chatbot fine-tuned on LLaMA3-8B for answering medical questions*

This project provides a conversational AI chatbot, **DocLLM-Chatbot**, capable of handling medical consultations. It is powered by a fine-tuned version of the LLaMA3-8B model and is built with **Streamlit** for an interactive user experience.

---

## **Features**
- Fine-tuned LLaMA3-8B model specifically for medical queries.
- Interactive chat interface built using Streamlit.
- Lightweight setup leveraging Ollama for efficient model handling.
- Includes a training notebook for replication or further fine-tuning as well as **Colab** [link](https://colab.research.google.com/drive/1aUL7FKJi5aRpZPPdKJHMbuF6u9EjGekH#scrollTo=6iVc4Ybv5odu).

---
## **Screenshots**
![Screenshot](screenshot1.png)
![Screenshot](screenshot2.png)

## **Installation Instructions**

### **1. Install Ollama**
Visit the [Ollama website](https://ollama.com/) and follow the installation instructions for your platform.

### **2. Set Up a Virtual Environment**
It’s recommended to use a virtual environment to manage dependencies. You can create one using conda:

```bash
conda create -n docllm-chatbot
conda activate docllm-chatbot
```
### **3. Install Dependencies**
Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

### **4. Download the Fine-Tuned Model**
Run the following command in your terminal to download the model:

```bash
huggingface-cli download Mondhirch/chatdoc-llama3-q4 unsloth.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

### **5. Create a Model Image**
Once the model is downloaded, create an image using Ollama:

```bash
ollama create chatdoc -f Modelfile
```

### **6. Run the Chatbot**
Start the chatbot by running the following command:

```bash
streamlit run main.py
```

### **7. Access the Application**
Once the chatbot is running, it should automatically open in your browser and navigate to http://localhost:8501, otherwise you can do it yourself to interact with DocLLM-Chatbot.