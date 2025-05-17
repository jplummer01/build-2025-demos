# Azure AI Search Agentic Retrieval: Meet the Experts Booth Content
Content to help experts prepare for staffing the  Azure AI Search Agentic Retrieval booth at BUILD 2025.

## At the booth

### Feedback
If a customer has a feature request or product feedback, send them here: [https://aka.ms/AI/Feedback](https://aka.ms/AI/Feedback)

### Decks
- [BUILD 2025 Product Announcements](decks/BUILD%202025%20-%20Product%20Announcements%20-%20One%20Sliders%20-%20Azure%20AI%20Search%20FY25.pptx)
- Azure AI Search Pitch Decks (General content covering the product)
  - [L100](decks/L100%20-%20Pitch%20Deck_Azure%20AI%20Search.PPTX
  - [L300](decks/L300%20-%20Azure%20AI%20Search%20FY25.pptx)
  - [L400](decks/L400%20-%20Azure%20AI%20Search%20FY25%20WIP.pptx)

### Running Demos
- [Agentic Retrieval Demo](https://capps-backend-pqyf4g35p3evg.redpebble-3e83d98f.eastus2.azurecontainerapps.io/)
- [Multimodal Demo](TBD)

### Code Samples
- [Agentic Retrieval Sample](https://github.com/Azure-Samples/azure-search-openai-demo)
- [Multimodal Sample](https://github.com/Azure-Samples/ai-search-multimodal-rag-demo)
- [Agent Memory](https://github.com/microsoft/Conversation-Knowledge-Mining-Solution-Accelerator)
- MCP
  - [Azure MCP](https://github.com/Azure/azure-mcp)
  - [Foundry MCP](https://github.com/azure-ai-foundry/mcp-foundry)

## Tier 2 Announcements 
- Agentic Retrieval (Public Preview)
  - New premium retrieval API for agentic AI applications.
  - Query planning with conversation history
  - Extractive answers
  - Token-based billing model
  - Demo: Agentic RAG with Agent Service contextual memory
- Multimodal Ingestion (Public Preview)
  - GenAI prompt skill: Enrich data on ingestion with chat completion & model inference
  - Demo: Multimodal ingestion in the Azure portal
  
## Reactive Topics/Announcements
- Azure AI Search MCP Server
- Enterprise security in Azure AI Search 
  - Doc level security trimming with ADLSGen2 ACL support (Public Preview)
  - Purview security labels (Private Preview)
- Indexer Skillset: Document Intelligence Skill (GA)
- Indexer Data Sources: Logic apps integration w/ support for 18 connectors (GA)
- Going GA post-BUILD (1-2 months)
  - Change your pricing tier (SKU migration) & Service Upgrade
  - Support for Confidential Compute
  - User-assigned Managed Identity Support

## Sessions
- [KEY010: Opening keynote](https://build.microsoft.com/en-US/sessions/KEY010?source=sessions) (May 19 | 9:05am)
- [BRK155: Azure AI Foundry: Agent factory](https://build.microsoft.com/en-US/sessions/BRK155?source=sessions) (May 19 | 11:15am)
- [BRK141: Knowledge retrieval: RAG for agents](https://build.microsoft.com/en-US/sessions/BRK141?source=sessions) (May 19 | 5:30pm)
- [DEM529: Memory and agentic retrieval with AI Search](https://build.microsoft.com/en-US/sessions/DEM529?source=sessions) (May 19 | 2:25pm)
- [COMM401: Conversations: AMA with Pablo](https://build.microsoft.com/en-US/sessions/COMM401?source=sessions) (May 20 | 5:45pm)
- [BRK142: Agentic RAG: build a reasoning retrieval engine](https://build.microsoft.com/en-US/sessions/BRK142?source=sessions) (May 21 | 12:30pm)

## Documentation
- [What's new in Azure AI Search | Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/whats-new)
- [Agentic Retrieval - Azure AI Search | Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/search-agentic-retrieval-concept)
  - [Quickstart: Run agentic retrieval in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-agentic-retrieval?pivots=python)
  - [Create an agent in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-agentic-retrieval-how-to-create)
  - [Retrieve data using an agent in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-agentic-retrieval-how-to-retrieve)
  - [Define an index for agentic retrieval in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-agentic-retrieval-how-to-index)
  - [Build an agent-to-agent retrieval solution using Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-agentic-retrieval-how-to-pipeline)
- [Multimodal search concepts and guidance in Azure AI Search - Azure AI Search | Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/multimodal-search-overview)
  - [Tutorial: Index mixed content using multimodal embeddings and the Document Extraction skill](https://learn.microsoft.com/en-us/azure/search/tutorial-multimodal-indexing-with-embedding-and-doc-extraction)
  - [Tutorial: Index mixed content using image verbalizations and the Document Extraction skill](https://learn.microsoft.com/en-us/azure/search/tutorial-multimodal-indexing-with-image-verbalization-and-doc-extraction)
  - [Tutorial: Index mixed content using multimodal embeddings and the Document Layout skill](https://learn.microsoft.com/en-us/azure/search/tutorial-multimodal-index-embeddings-skill)
  - [Tutorial: Index mixed content using image verbalizations and the Document Layout skill](https://learn.microsoft.com/en-us/azure/search/tutorial-multimodal-index-image-verbalization-skill)
- [Document-level access control - Azure AI Search | Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview)
- [Connect to Logic Apps - Azure AI Search | Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/search-how-to-index-logic-apps-indexers)
- [Upgrade your Azure AI Search service in the Azure portal](https://learn.microsoft.com/en-us/azure/search/search-how-to-upgrade)
- [Change your pricing tier (SKU)](https://learn.microsoft.com/en-us/azure/search/search-sku-tier#tier-changes)

## Blogs
- [Agentic Retrieval Announcement](aka.ms/AgentRAG)
- [Agentic Retrieval Evals and Test](aka.ms/AISearch-ARevals)
- [Multimodal Announcement]()
- [Introducing Model Context Protocol (MCP) in Azure AI Foundry: Create an MCP Server with Azure AI Agent Service | Azure AI Foundry Blog](https://devblogs.microsoft.com/foundry/integrating-azure-ai-agents-mcp/)

## FAQ

### Azure AI Search Agentic Retrieval
**Q: Can you take in a prompt (along with chat history) as well - so the subqueries are domain specific?**
A: Currently, agentic retrieval does not allow for a prompt to be included along with the chat history. However, instructions can be included in the conversation, but there is no guarantee it will steer the subqueries effectively.
 
**Q: Does the activity log include tokens in/out?**
A: Yes, the activity log includes the tokens used for query planning, allowing you to see the token usage.
 
**Q: Can we use 4.1 mini soon?**
A: Yes, you will be able to use 4.1 mini when the feature launches.
 
**Q: Is the AOAI Model used configurable?**
A: Yes, the AOAI model used for agentic retrieval is configurable.
 
**Q: So Semantic Ranking is required for this. If so, is Hybrid also required?**
A: Semantic ranking is required for agentic retrieval. Hybrid search is used if there is a vectorizer defined in your index. If you have indexed only text fields, hybrid search will not be run.
 
**Q: How will you manage top-K - it will topk per subquery or on the final answer?**
A: Agentic retrieval manages top-K in terms of output tokens rather than a specific top-K parameter. The maximum number of tokens returned in the grounding response string is controlled.
 
**Q: For the subquery, can this be to a tool? a Fabric Data Agent? or is this created by the Agentic Retrieval?**
A: The subqueries are generated by agentic retrieval using a prompt sent to your AOAI model. There is no option to use fabric data agents or another tool.
 
**Q: Can you still have multiple searchable vector fields?**
A: Yes, agentic retrieval can search across multiple vector fields simultaneously.
 
**Q: Have you found the quality of the results improve while using this compared to previous approaches? If so, is there any data / benchmarks on this we will be able to share?**
A: Yes, agentic retrieval shows a 40% improvement in answer relevance on complex queries compared to regular search. Metrics and benchmarks will be shared in a blog.
 
**Q: Are we using LLM to do Semantic Ranking? Can that be replaced by my LLM? or LLM is for query planning?**
A: The LLM is used for query planning, not for semantic ranking. Semantic ranking uses the same model as before, with a token-based pricing model. 
 
**Q: Any thoughts on providing customers with how they should think about their chunk size, to quality to price?**
A: Customers can control the length of their conversation history and set a cap on the number of documents sent to semantic ranker to manage token usage and costs. 
 
### Document-Level Permissions Support
**Q: Is the client token - the jwt token from (say our EntraID)?**
A: Yes, the client token is the JWT token from EntraID, passed through the header x-ms-query-source-authorization.
 
**Q: Will the headers be supported in the SDK as well Python SDK?**
A: Yes, the headers will be supported in the Python SDK.
 
### Multimodal Search
**Q: How (or does) this work with the Agentic Retrieval? I believe Matt mentioned it had to be the same vector type, so would Agentic Retrieval support this combination of text and multimodal vectors?**
A: Agentic retrieval supports multimodal embeddings if the vectorizer is defined in the index. However, image messages in conversation history are not supported at build but are on the roadmap.
 
**Q: Are we doing image embedding for images, or are we describing the images and then indexing the description?**
A: Both options are available. You can use image verbalization to describe images or use multimodal embeddings directly.
 
**Q: What multimodal embedding model are you using?**
A: The multimodal embedding models supported include Azure OpenAI, AI Foundry, and AI Vision.
 
**Q: So if we do multimodal embedding then we can send an image in the chat history to perform a search. However if we do image verbalizer then it is better to verbalize the user image and then perform the search (using text vectorizer)?**
A: Yes, you need to decide how to address the user's query and plan the indexing accordingly. Both options are available, but they are separated to avoid high costs during testing.