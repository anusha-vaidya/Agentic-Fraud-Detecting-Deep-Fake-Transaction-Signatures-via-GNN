Agentic Fraud & "Deep-Fake" Transaction Signatures
Advanced Behavioral Detection via Graph Neural Networks (GNN)

🛡️ Project Overview 
In 2026, the fraud landscape has shifted from simple phishing to Agentic "Burst Attacks." These are automated, AI-driven bots that simulate human behavior to execute thousands of transactions per second. Traditional rule-based engines fail because they look at transactions in isolation. This project implements a "Living Defense Ledger" that identifies the "Hydra” interconnected networks of accounts exhibiting identical, non-human behavioral signatures.

🚀 Key Technical Features
•	Graph-Based Analysis: Utilizing NetworkX to map relationships between 10k+ synthetic accounts.
•	Clustering (DBSCAN): Identifying high-density "latency clusters" where multiple accounts act with sub-millisecond synchronization.
•	GNN Architecture: Preparing the foundation for Graph Neural Networks to score the risk level of account neighborhoods.
•	Living Defense: An automated pipeline (GitHub Actions) that updates detection signatures monthly against evolving patterns.

🛠️ Execution

• git clone https://github.com/anusha-vaidya/Agentic-Fraud-Detecting-Deep-Fake-Transaction-Signatures-via-GNN.git
• cd Agentic-Fraud-Detecting-Deep-Fake-Transaction-Signatures-via-GNN
• pip install -r requirements.txt
• python src/generate_data.py
• Run notebooks in order: 01 (EDA) -> 02 (Graph) -> 03 (ML)

