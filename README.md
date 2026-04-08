Agentic Fraud & "Deep-Fake" Transaction Signatures
Advanced Behavioral Detection via Graph Neural Networks (GNN)

🛡️ Project Overview 
In 2026, the fraud landscape has shifted from simple phishing to Agentic "Burst Attacks." These are automated, AI-driven bots that simulate human behavior to execute thousands of transactions per second. Traditional rule-based engines fail because they look at transactions in isolation. This project implements a "Living Defense Ledger" that identifies the "Hydra” interconnected networks of accounts exhibiting identical, non-human behavioral signatures.

🚀 Key Technical Features
•	Graph-Based Analysis: Utilizing NetworkX to map relationships between 10k+ synthetic accounts.
•	Clustering (DBSCAN): Identifying high-density "latency clusters" where multiple accounts act with sub-millisecond synchronization.
•	GNN Architecture: Preparing the foundation for Graph Neural Networks to score the risk level of account neighborhoods.
•	Living Defense: An automated pipeline (GitHub Actions) that updates detection signatures monthly against evolving patterns.

🛠️ Installation & Execution
1.	Setup Environment
# Clone the repository
git clone https://github.com/anusha-vaidya/Agentic-Fraud-Detecting-Deep-Fake-Transaction-Signatures-via-GNN.git
# Enter the directory
cd Agentic-Fraud-Detecting-Deep-Fake-Transaction-Signatures-via-GNN
# Install dependencies
pip install -r requirements.txt

2.	Generate Data
python src/generate_data.py
Note: This process is also automated via GitHub Actions on the first of every month.

3. Execution Pipeline
The detection logic is broken down into three sequential stages. Open these in Jupyter or VS Code to see the results:
01_adversarial_detection_EDA.ipynb: Identifies "Burst" signatures using velocity analysis.
02_graph_network_construction.ipynb: Maps the "Hydra" network to find interconnected account clusters.
03_unsupervised_anomaly_detection.ipynb: Uses DBSCAN to automatically label suspicious activity without pre-labeled data.

