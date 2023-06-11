# Talk to your insurance PDFs 🏥

This repository contains a Python script 🐍 which fetches and compares health insurance plans offered by two companies: EmblemHealth and MetroPlus. The script is designed to automate the process of gathering information and making comparisons, providing a detailed summary of the offerings from each company.

The Python code uses various libraries like OpenAI, Langchain, Tiktoken, and Yaml to help in this process. The main highlight of this code is the ability to ask a set of defined questions to each insurance policy, and get detailed answers using language models. 👥

## What does the script do? 🤔

Loading Data from PDFs: 📄 The script takes as input PDF documents from the two insurance companies and converts them into text data using the PdfToTextLoader.

Vectorizing dataset: 📊 The script then vectorizes the text data. This involves transforming the text data into a form that machine learning algorithms can understand.

Asking questions: ❓ The script then asks a set of predefined questions about the insurance policies of each company. These questions relate to details about deductibles, coverage, limitations, and other important aspects.

Comparing Answers: 🆚 After gathering the responses, the script summarizes the answers from each company, providing a quick and easy way to compare the offerings of each company.

Ratings: ⭐️ The script also provides a rating system that grades each insurance policy in terms of coverage of different health procedures, flexibility for remote workers abroad, and price and compensation.

## What does the app do?

![](https://github.com/Rachnog/pdfs_question_answering/blob/main/streamlit.gif)

App Flow 🌊
Upload Insurance Plans: Users upload two insurance plan documents in PDF format. They can also provide names for these plans.

PDF Loading and Vectorizing: The app converts PDF files into text, and then generates vector representations of the text for further processing.

User Input: Users provide a brief company description and a list of questions that they want to use to compare the plans. They also provide a set of final criteria for decision-making.

Processing and Answer Generation: The app processes the questions against each plan, gathers answers, and generates a final decision based on the provided criteria. It utilizes OpenAI's language model to analyze and understand the information in the documents and to create the final decision.

Output: The app outputs the answers to the provided questions and the final comparative decision based on the criteria. It presents these in an easy-to-understand format.
