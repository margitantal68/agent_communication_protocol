# Agent Communication Protocol

A RAG Agent with CrewAI adapted for Gemini, designed to facilitate communication between agents using a custom protocol. This project allows agents to exchange messages in a structured format, enabling efficient task management and response handling.

Link to the original project: [ACP: Agent Communication Protocol](https://www.deeplearning.ai/short-courses/acp-agent-communication-protocol/)


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
