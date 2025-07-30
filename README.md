# Agent Communication Protocol

- This project builds a RAG agent with `CrewAI` using **Gemini**. It will do that by integrating RagTool from `crewai_tools` with a `CrewAI` agent. 
- RagTool provides a way to create and query knowledge bases from various data sources, and allows the agent to access specialized context. 
- You will provide the RAG tool a pdf (`data` folder).


Link to the original course: [ACP: Agent Communication Protocol](https://www.deeplearning.ai/short-courses/acp-agent-communication-protocol/)


### Prerequisites

1. Python >=`3.11` and <`3.13`
1. Git
1. Gemini API key

### Steps
1. Clone the repository
    ```bash
    git clone https://github.com/margitantal68/agent_communication_protocol.git
    ```

1. Navigate to the project directory
    ```bash
    cd agent_communication_protocol
    ```

1. Create and activate a virtual environment
    * On Linux/macOS:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

    * On Windows:
        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        ```

1. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```


## Usage

This project requires a Gemini API key. 

1. Obtain yor GEMINI API key from[Google AI Studio](https://aistudio.google.com/app/apikey)
1. Copy the **.env.example** file in the project directory:
    ```bash
    cp .env.example .env
    ```

1. Set the API key in the **.env** file:
    ```bash
    GOOGLE_API_KEY=your_api_key_here
    ```

1. Run the project:
    ```bash
    python rag_gemini.py
    ```
