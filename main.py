from langchain_community import OpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


# SECURE KEY LATER
api_key =

llm = OpenAI(
    openai_api_key=api_key
)

code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=["language", "task"]
)

code_chain = LLMChain(
    llm = llm,
    prompt = code_prompt
)

result = code_chain({
    "language": "python",
    "task": "return a list of numbers"

})
print(result)

