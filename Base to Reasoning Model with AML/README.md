## Training an Instruct model into a Reasoning model on AML using GRPO

GRPO (Group Relative Policy Optimization) is a lightweight, memory-efficient reinforcement learning technique designed to train reasoning models by optimising responses without needing a separate value or critique model—making it faster and more scalable than traditional PPO. It leverages reward functions to guide learning, enabling scalable and stable training of reasoning capabilities. In this demo, we will demonstrate how Azure ML can be used to fine-tune a non-reasoning model into a reasoning model with ease.

Video: [https://www.youtube.com/watch?v=YOm_IQt3YWw](https://www.youtube.com/watch?v=YOm_IQt3YWw)

Code: [https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/grpo](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/grpo)
