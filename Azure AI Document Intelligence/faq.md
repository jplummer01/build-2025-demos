
# FAQ for CU and DI at Build

## Compiling some potentially asked questions for CU at Build 2025

### Q: What is Azure AI Content Understanding?
A: It’s a multimodal service that uses AI to extract insights, classify, generate, any unstructured or semi-structured content — like documents, audio, video, text, web pages, and digital archives — into structured format to be consumed by other workflows like LLM, agents, etc.

### Q: How is it different from Azure Document Intelligence?
A: Document Intelligence focuses on structured document extraction (forms, invoices, etc.), while Content Understanding focuses on broad, unstructured or mixed-content processing (text, images, audio, video, web pages) for search and knowledge mining.

### Q: What are the new modes in Content Understanding?
A: Standard: This mode serves as the default solution for processing diverse content types. It's optimized to provide efficient schema extraction tailored to specific tasks across all data formats. This mode emphasizes cost-effectiveness and reduced latency, ensuring structured insights are accessible for your general processing needs.
Pro: This mode is designed for advanced use cases, particularly those requiring multi-step reasoning, and complex decision-making (for instance, identifying inconsistencies, drawing inferences, and making sophisticated decisions). The pro mode allows input from multiple content files and includes the option to provide reference data at analyzer creation time. Currently, pro mode is only offered for your document-based data.

### Q: What are the typical use cases?
A: 
- Enterprise content search
- Knowledge mining
- Compliance data discovery
- Content summarization
- Classification
- Metadata extraction across diverse content repositories

### Q: List some key features for CU?
A: 
- Key phrase extraction
- Entity recognition
- Sentiment analysis
- Language detection
- OCR
- Image analysis
- Video analysis
- Speaker analysis
- Inferencing and reasoning
- Generative capabilities and more

### Q: Region and language supported? GA timeframe?
A: Currently its available as a preview service in 3 regions (West US, Sweden Central, Australia East) and support all major languages across all modalities. GA is targeted around July/Aug.

### Q: Any upcoming preview release?
A: With Build, we are announcing our latest preview.2 which is now available to use. It expands support for selection mark, improved confidence score, table layout, agentic reasoning for documents, speaker diarization, extract fields and entities from conversations, generate video metadata, tag scenes, and categorize video content. <add for audio and video too>

### Q: Support for different file types?
A: <Adding list of all the file types we support across modality post preview.2> Common document formats (PDF, Excel, text, HTML), image files (JPEG, PNG, TIFF, PDF with images), audio (WAV, MP3, FLAC), video (MP4, MOV), and multiple languages via built-in AI language and transcription services

### Q: SDK and REST API availability?
A: Only python based REST API repo is available for now. Will be adding SDKs shortly.

### Q: How is the service priced? Are there free tiers or trials available?
A: Please refer to our pricing page for more details. 

### Q: What is the difference between content and field extraction?

### Q: What are different modes available for CU?
A: We have a new Pro mode available now. The pro mode, currently exclusive to the document analyzer, enables advanced capabilities. Content Understanding now supports reasoning across multiple documents as input for external knowledge, empowering users to derive agentic inferences directly from reference documents while standard mode is focused for extraction across all modalities.

### Q: Upcoming roadmap?

### Q: Committed SLA/latency? How much files and sizes it can handle?
A: Please check our service page.

### Q: Can we bring our own model? Which model do you use underneath? Can we change it?
A: No not yet, we are working on a plan to support bring your own model for future release.

### Q: How to ensure better confidence/accuracy for the datasets? How is confidence score calculated?

### Q: Can do we compose models when we have multiple different files/content types?
A: Yes, you can use classification API and pass the data over to respective custom analyzers.

### Q: What happens to DI? Do we need to migrate over?
A: No, we will not be deprecating DI, if you are happy using DI, there’s no need to move to CU.

### Q: Do you support human review?
A: Human in the loop is planned for DI, will be in our roadmap for CU.
