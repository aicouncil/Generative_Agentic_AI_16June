Here's the updated information with the Flowise installation guide, in markdown format:

The document "Generative & Agentic AI - 16th June - Notes by Gemini" summarizes a meeting from July 23, 2025, focusing on multi-agent frameworks and their development.

Here's a breakdown of the key topics:

### Multi-Agent Framework Overview:

  * The current focus is on multi-agent frameworks, moving beyond single LLM-based applications.
  * A multi-agent system is likened to a company structure with a "supervisor" agent (like a CEO) controlling "worker" agents (CFO, CTO).
  * Each worker agent can be powered by different LLMs and assigned specific tasks, enabling greater automation and specialized functions.

### Benefits of Multi-Agent Systems:

  * These systems offer better and faster performance due to distributed tasks.
  * The supervisor agent ensures a sequential workflow, preventing tasks from being performed out of order and ensuring each agent completes its small, specific work before the next one begins.
  * This structured approach helps avoid issues like generative models forgetting information or providing unexpected results with large prompts.

### Agent Functionality and Tools:

  * Agents can perform "function calling," allowing them to access external tools like saving files, using calculators, or retrieving stock prices.
  * An example of an emailing agent was used to demonstrate how agents can integrate tools for specific tasks (e.g., searching job openings, writing emails, formatting emails, and potentially sending them).
  * This integration of tools makes agents smarter compared to conventional generative AI models.

### Agent Development Frameworks:

  * Several frameworks for building agents were introduced, with LangChain highlighted as a popular choice.
  * Other mentioned frameworks include LangFlow, VectorShift, VoiceFlow, and Flowise (which can be used offline and is free).
  * Autogen by Microsoft was also noted as a potentially growing framework due to its ecosystem backing.

### Technical Requirements for Agent Development:

  * To start building agents, especially with offline tools like Flowise, users must read documentation and install Node.js (specifically versions 18, 19, or 20).
  * Agent development often involves using APIs to enable agents to access various tools like web search, calculators, or email services.

### Installation Guide for Flowise:

Flowise is an open-source low-code tool for building customized LLM (Large Language Model) orchestration flows. Here's how to install it:

**Prerequisites:**

  * **Node.js:** Flowise requires Node.js (versions 18, 19, or 20). If you don't have it, download and install the appropriate version from the official Node.js website.

**Installation Steps:**

1.  **Using `npm` (Node Package Manager):**
    Open your command prompt or terminal and run the following command to install Flowise globally:

    ```bash
    npm install -g flowise
    ```

2.  **Start Flowise:**
    After installation, you can start the Flowise application by running:

    ```bash
    flowise start
    ```

    Flowise will typically run on `http://localhost:3000` by default.

3.  **Using `npx` (Node Package Execute - for quick setup):**
    Alternatively, you can start Flowise directly without global installation using `npx`:

    ```bash
    npx flowise start
    ```

    This method is good for trying out Flowise quickly without installing it globally.

4.  **Local Development (from source):**
    If you intend to contribute to Flowise or need more control over the installation, you can clone the repository and run it locally:

    ```bash
    git clone https://github.com/FlowiseAI/Flowise.git
    cd Flowise
    npm install
    npm run start
    ```

**Important Notes:**

  * Node.js is used for the Flowise user interface (UI).
  * Flowise is a no-code drag-and-drop tool for creating agents, contrasting with code editors like VS Code which are used for writing code.

### Agent Part Completion Timeline and Support:

  * The completion of the agent part is estimated to take two to three weeks, with installation support offered for any issues.
  * The possibility of using N8 (a paid software) was mentioned, with a check for a trial version.

### Installing Libraries and VS Code Usage:

  * The process of installing libraries using `pip install` in the VS Code terminal was demonstrated.
  * VS Code was deemed suitable for final packaging and modularizing code (especially for MLOps) due to its debugging and organization features, in contrast to Colab or Jupyter Notebooks which are better for initial project setup.
  * It was also noted that VS Code has extensions for Jupyter Notebooks, allowing users to create `.ipynb` files within VS Code.
