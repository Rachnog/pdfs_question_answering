# Talk to your insurance PDFs 🏥

This repository contains a Python script 🐍 which fetches and compares health insurance plans offered by two companies: EmblemHealth and MetroPlus. The script is designed to automate the process of gathering information and making comparisons, providing a detailed summary of the offerings from each company.

The Python code uses various libraries like OpenAI, Langchain, Tiktoken, and Yaml to help in this process. The main highlight of this code is the ability to ask a set of defined questions to each insurance policy, and get detailed answers using language models. 👥

## What does the script do? 🤔

Loading Data from PDFs: 📄 The script takes as input PDF documents from the two insurance companies and converts them into text data using the PdfToTextLoader.

Vectorizing dataset: 📊 The script then vectorizes the text data. This involves transforming the text data into a form that machine learning algorithms can understand.

Asking questions: ❓ The script then asks a set of predefined questions about the insurance policies of each company. These questions relate to details about deductibles, coverage, limitations, and other important aspects.

Comparing Answers: 🆚 After gathering the responses, the script summarizes the answers from each company, providing a quick and easy way to compare the offerings of each company.

Ratings: ⭐️ The script also provides a rating system that grades each insurance policy in terms of coverage of different health procedures, flexibility for remote workers abroad, and price and compensation.
