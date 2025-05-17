# Azure AI Foundry Observability: Meet the Experts Booth Content
Content to help experts prepare for staffing the  Azure AI Foundry Models at BUILD 2025.

## Content Deck
[Azure AI Foundry Observability Build Content](https://microsoft.sharepoint.com/:p:/t/expinternal/EZ-QRMjZIrtIr0VHszPGuqsBma0U2RguWovq6P5YyxiuiQ?e=hktVaZ)

## E2E Video Demo
[Demo Video](https://microsoft-my.sharepoint.com/:v:/p/skohlmeier/ET4l-HSQxyxCv4ZV6TWIj2YBU2_NPowjA56ZhIy2ku3ypQ?e=7Ta3D7&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

## Key Announcements - More details in deck above

We’re thrilled to launch the public preview of Azure AI Foundry Observability, the first unified solution for governance, evaluation, tracing, and monitoring — all built into your AI development loop. From model selection to real-time debugging, our observability capabilities empower teams to ship production-grade AI with confidence and speed.

- **AI Governance** 
  - Connect with Microsoft Purview Compliance Manager,  Credo AI and Saidot, to define evaluation plans aligned with frameworks like the EU AI Act — and run them directly via the Azure AI Evaluation SDK. 
- **Leaderboards**
  - Azure AI Foundry’s new leaderboards let you compare foundation models by quality, cost, and performance — all backed by industry benchmarks.
- **Evaluate and Trace in the Agents Playground**
  - The Agents Playground now comes with built-in evaluation and tracing — so you can test, debug, and improve your agents in one place.
- **New Evaluators (Agents and AOAI Graders)**
  - You can now directly assess agent thread messages using built-in metrics like
    - Intent Resolution: Measures how accurately the agent identifies and addresses user intentions.
    - Task Adherence: Measures how well the agent follows through on identified tasks.
    - Tool Call Accuracy: Measures how well the agent selects and calls the correct tools to.
    - Response Completeness: Measures to what extent the response is complete (not missing critical information) with respect to the ground truth. 
  - With our new integrations with Azure OpenAI Graders, you get even more precision (label grader, string checker, text similarity, custom general grader)
- **AI Red Teaming Agent**
  - Meet the Azure AI Foundry AI Red Teaming Agent — your built-in defense against unsafe AI. Powered by Microsoft’s open-source PyRIT, it simulates adversarial attacks to uncover vulnerabilities before you ship.
    - Scan for content safety risks automatically
    - Measure exposure with metrics like Attack Success Rate (ASR)
    - Generate detailed readiness reports
- **CI/CD Workflow Integration**
  - With our GitHub Action and Azure DevOps Extension, you can:
    - Auto-evaluate agents on every commit
    - Compare versions with built-in quality, performance, and safety metrics
    - Get confidence intervals and significance tests to back your decisions
- **Continuously Monitor and Evaluate in Production**
  - A unified dashboard tracks performance, quality, safety, and resource usage — all in real time.
    - Run continuous evaluations on live traffic (e.g., 10 per hour)
    - Set alerts in Azure Monitor to catch drift or regressions
    - Link directly to Azure Monitor Application Insights for full-stack visibility
  - Dashboard is backed by Azure Monitor to enable alerting and in-depth monitoring of Azure infrastructure
- **Trace Every Evaluation**
  - With tracing enabled, every continuous evaluation result is mapped to a trace — giving you full visibility into your agent’s execution flow. 
  
## Sessions
- [KEY010: Opening keynote](https://build.microsoft.com/en-US/sessions/KEY010?source=sessions) (May 19 | 9:05 AM)
- [BRK155: Azure AI Foundry: The Agent Factory](https://build.microsoft.com/en-US/sessions/BRK155?source=sessions) (May 19 | 11:45 AM)
- [LAB334: Evaluate and improve the quality and safety of your AI applications](https://build.microsoft.com/en-US/sessions/LAB334?source=sessions) (May 19 | 4:30 PM)
- [DEM528: Continuously improve your Agent in production](https://build.microsoft.com/en-US/sessions/DEM528?source=sessions) (May 20 | 5:30 PM)
- [BRK168: AI and Agent Observability in Azure AI Foundry and Azure Monitor](https://build.microsoft.com/en-US/sessions/BRK168?source=sessions) (May 21 | 12:30 PM)
- [DEM527: From risk to reward: AI governance integrations for Azure AI Foundry](https://build.microsoft.com/en-US/sessions/DEM527?source=sessions) (May 21 | 2:50 PM)
- [DEM552: Accelerate AI red teaming for your GenAI apps]([https://build.microsoft.com/en-US/sessions/LAB334?source=sessions](https://build.microsoft.com/en-US/sessions/DEM552?source=sessions) (May 21 | 3:30 PM)
