This document summarizes a meeting between AI Council and Pritam Kusiyait on August 5, 2025, focusing on the creation and deployment of a social media strategy agent using Flowise.

Here's a breakdown of the key discussion points:

  * **Agent Creation in Flowise:** AI Council guided Pritam Kusiyait through setting up a social media strategy agent in Flowise, emphasizing its cost-effectiveness compared to other tools. This involved adding a supervisor agent and three worker agents, then connecting the supervisor to each worker.
  * **LLM Integration and Credentials:** They integrated a GPT model (ChatOpenAI) as the Language Model (LLM) for the agent, noting its good performance with agents. Pritam Kusiyait connected existing credentials.
  * **Prompt Engineering and Agent Tasks:** AI Council introduced the concept of using a "prompt engineering team" agent from the Flowise marketplace to automatically generate prompts for the worker agents. They defined specific tasks for four agents: a blog writer, a YouTube video script creator, a YouTube title generator, and a social media post creator for X (formerly Twitter).
  * **Troubleshooting and LLM Performance:** During testing, the social media post creator agent experienced issues. AI Council attempted various troubleshooting steps, including adding individual LLMs to specific workers and changing the main LLM model to GPT 4.1 mini, which ultimately resolved the problem.
  * **API Setup, Billing, and Deployment:** The discussion covered setting up APIs for the agent, adding funds to the GPT account, and the billing structure based on input and output tokens. AI Council explained that deployment would be covered in a future session and that a web interface would be created for sharing the service.
  * **Cost Optimization:** Pritam Kusiyait raised concerns about the model's rapid consumption of funds. AI Council suggested switching to less expensive "mini" or "nano" models or exploring alternative, cheaper services.
