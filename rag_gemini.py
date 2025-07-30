import os

from crewai import Crew, Task, Agent, LLM
from crewai_tools import RagTool

import warnings
warnings.filterwarnings('ignore')

from dotenv import load_dotenv, dotenv_values

load_dotenv()

print(dotenv_values()) 


llm = LLM(model="gemini/gemini-2.0-flash")

# Gemini API key is set in the .env file
config = {
    "llm": {
        "provider": "google",
        "config": {
            "model": "gemini/gemini-2.0-flash",
        }
    },
    "embedding_model": {
        "provider": "google",
        "config": {
            "model": "models/embedding-001"
        }
    }
}



print("###Config:", config)
print("\n\n")

# RAG tool configuration
rag_tool = RagTool(config=config,  
                   chunk_size=1200,       
                   chunk_overlap=200,     
                  )

print("Adding PDF to knowledge base. Please wait...")
rag_tool.add("./data/Zarovizsga_szabalyzat_2024_25.pdf", data_type="pdf_file")
print("PDF added successfully.\n\n")


print("RAG tool has been created and configured with the provided PDF.\n\n")


# AGENT
regulation_agent = Agent(
    role="University Regulations Assistant", 
    goal="Answer questions related to university regulations and policies",
    backstory="You are an expert agent designed to assist with Methodology of organizing final examinations at the University. You have access to the university regulations and policies, and you can provide accurate and detailed answers to questions about these topics." \
    "You are able to use the RAG tool to retrieve relevant information from the university's knowledge base. Please answer in Hungarian.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[rag_tool], 
    max_retry_limit=5
)

while True:
    user_question = input("Kérdésed a szabályzattal kapcsolatban (vagy 'exit' a kilépéshez): ")
    if user_question.strip().lower() == 'exit':
        break

    # Define the task for the agent
    task = Task(
        description=(
            f"Keresd ki a következő kérdésre a választ a belső tudásbázisból a 'Knowledge base' (RAG) eszköz segítségével: '{user_question}'. "
            "Fontos: A 'Knowledge base' eszközhöz a 'query' paraméternek egy egyszerű szöveges lekérdezésnek kell lennie, amely egyértelműen megfogalmazza a keresett információt. "
            "A válaszodat magyarul fogalmazd meg tömören és érthetően, a szabályzatban található információk alapján."
        ),
        expected_output="Tömör, magyar nyelvű válasz a záróvizsga szabályzatról",
        agent=regulation_agent,
        tools=[rag_tool] # Explicitly list the tool for the task as well for clarity
    )
    crew = Crew(agents=[regulation_agent], tasks=[task], verbose=True)
    answer = crew.kickoff()
    print(answer)


