Agentic Fraud & "Deep-Fake" Transaction Signatures
Advanced Behavioral Detection via Graph Neural Networks (GNN)

🛡️ Project Overview
In 2026, the fraud landscape has shifted from simple phishing to Agentic "Burst Attacks." These are automated, Al-driven bots that can simulate human behavior to execute thousands of transactions per second. Traditional rule-based engines fail because they look at transactions in isolation.

This project implements a "Living Defense Ledger" that identifies the "Hydra"—interconnected networks of accounts exhibiting identical, non-human behavioral signatures.

🚀 Key Technical Features
Graph-Based Analysis: Utilizing nodes and edges to map relationships between 10k+ synthetic accounts.
Clustering (DBSCAN): Identifying high-density "latency clusters" where multiple accounts act with sub-millisecond synchronization.
GNN Architecture: Implementing a Graph Neural Network to score the risk level of entire account neighborhoods rather than single users.
Living Defense: An automated pipeline (GitHub Actions) that updates detection signatures against evolving adversarial patterns.

📂 Repository Structure
data/: Synthetic transaction logs and behavioral datasets.
notebooks/: Exploratory Data Analysis (EDA) and GNN model training experiments.
src/: Production-ready scripts for data generation and real-time inference.
docs/: White papers on the 2026 fraud landscape and architecture diagrams.

🛠️ Tech Stack
Language: Python
Data Science: Pandas, NumPy, Scikit-learn
Graph Learning: PyTorch Geometric (PyG), NetworkX
DevOps: GitHub Actions

How to Run This:

