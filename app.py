import yaml
import streamlit as st

from langchain import OpenAI, VectorDBQA, LLMChain
from langchain.prompts import PromptTemplate

from pdf_loaders import PdfToTextLoader
from dataset_vectorizers import DatasetVectorizer

with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

OPENAI_API_KEY = config['OPENAI_KEY']
PDFS, NAMES, TXTS = [], [], []
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 500

# ----- Header of the app -----
st.title("Comparing insurance plans")
st.write("This app compares insurance plans using the OpenAI API. It is a prototype and not intended for actual use.")

# ----- Select and upload the files one by one -----
st.header("Select the files to compare")
st.write("The files should be in PDF format.")
file_1 = st.file_uploader("File 1")
file_2 = st.file_uploader("File 2")
name_1 = st.text_input("Name of file 1", value="Plan 1")
name_2 = st.text_input("Name of file 2", value="Plan 2")

# ----- Load the files -----
if file_1 and file_2:

    with open("./data/" + file_1.name, "wb") as f:
        f.write(file_1.getbuffer())

    with open("./data/" + file_2.name, "wb") as f:
        f.write(file_2.getbuffer())

    PDFS = ["./data/" + file_1.name, "./data/" + file_2.name]
    NAMES = [name_1, name_2]

    for pdf_path in PDFS:
        txt_path = pdf_path.replace(".pdf", ".txt")
        pdf_loader = PdfToTextLoader(pdf_path, txt_path)
        text = pdf_loader.load_pdf()
        TXTS.append(txt_path)
    st.write("Files loaded successfully.")

    dataset_vectorizer = DatasetVectorizer()
    documents_1, texts_1, docsearch_1 = dataset_vectorizer.vectorize([TXTS[0]], chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP, openai_key=OPENAI_API_KEY)
    documents_2, texts_2, docsearch_2 = dataset_vectorizer.vectorize([TXTS[1]], chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP, openai_key=OPENAI_API_KEY)
    llm = OpenAI(model_name='text-davinci-003', temperature=0, openai_api_key=OPENAI_API_KEY)
    qa_chain_1 = VectorDBQA.from_chain_type(llm=llm, chain_type='stuff', vectorstore=docsearch_1)
    qa_chain_2 = VectorDBQA.from_chain_type(llm=llm, chain_type='stuff', vectorstore=docsearch_2)
    st.write("Files vectorized successfully.")

    # ----- Write questions separated by a new line -----
    st.header("Write the questions to generate a summary")

    st.write("Brief company description")
    company_description = st.text_area("Brief company description", value="full-remote consulting company with 100 employees")

    st.write("The questions should be separated by a new line.")
    questions = st.text_area("Questions", 
                             value = """
How good are the deductibles?
How is the preventive care coverage?
How this plan fits for remote workers in the US and abroad?
What is the maximum money amount that can be compensated?
Can I go to any hospital of my choice?
Are there any limitations that won\'t allow to use the insurance?
Does it cover the family members of the applicant?
What are the healthcare procedures that are not covered by the insurance?
Can I use the insurance for the dental care?
Can I use the insurance in other countries?""")
    QUESTIONS = questions.split("\n")
    QUESTIONS = [q.strip() for q in QUESTIONS if len(q) > 0]

    # ----- Select final criteria for decision-making -----
    st.header("Select the final criteria for decision-making")
    st.write("The criteria should be separated by a new line.")
    criteria = st.text_area("Criteria", value="""
1. Coverage of different health procedures
2. Flexibility for remote workers abroad
3. Price and compensation""")
    CRITERIA = criteria.split("\n")
    CRITERIA = [c.strip() for c in CRITERIA if len(c) > 0]
    final_criteria = "".join([f"{i}. {c}\n" for i, c in enumerate(CRITERIA, 1)])

    # ----- Generate the intermediate answers for the document summary -----
    summary_of_answers = ""
    for q in QUESTIONS:
        print(q)
        answer_1, answer_2 = qa_chain_1.run(q), qa_chain_2.run(q)
        summary_of_answers += "Question: " + q + "\n"
        summary_of_answers += f"{NAMES[0]} answer: " + answer_1 + f";\n {NAMES[1]} answer: " + answer_2 + "\n"
        
    template = """
        I want you to act as an expert in insurance policies. I have asked two companies about their insurance policies and here are their answers:
        {summary_of_answers}
        I am looking for insurance for a {company_description}. I want you to tell me which company is better and why.
        Give me a rating (x out of 10) for the following categories for each company separately with a short explanation (10 words max) for each category:
        {final_criteria}
        Your answer and final recommendation after the rating:
        """
    
    prompt = PromptTemplate(
        input_variables=["summary_of_answers", "company_description", "final_criteria"],
        template=template,
    )
    
    answer = ""
    llm = OpenAI(model_name='text-davinci-003', temperature=0, openai_api_key=OPENAI_API_KEY, request_timeout=60)
    chain = LLMChain(llm=llm, prompt=prompt)
    answer = chain.run({"summary_of_answers": summary_of_answers, "final_criteria": final_criteria, "company_description": company_description})

    # ----- Generate the final answer -----
    st.header("Final answer")
    st.write(answer)



