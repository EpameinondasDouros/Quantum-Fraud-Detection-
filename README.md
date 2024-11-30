Quantum Fraud Detection: Leveraging Federated Learning with Blockchain

🏆 Competition Overview


This project was created for the Quantum Fraud Detection Competition organized by NYU Abu Dhabi. The goal was to detect fraudulent activities by developing innovative quantum models and integrating them with cutting-edge federated learning frameworks and blockchain technology.

🌌 Key Features


Quantum Models for Fraud Detection
Quantum-inspired approaches enable highly accurate fraud prediction with enhanced efficiency.

Federated Learning
Privacy-preserving machine learning allows secure collaboration across distributed datasets.

Blockchain Integration
Immutable and decentralized data sharing for federated learning.

🚀 Technical Highlights



Fig: A high-level view of Quantum-Blockchain Federated Learning

### Note: 

Blockchain Setup: The Ethereum blockchain for model aggregation is simulated using Ganache. Ganache is a local Ethereum blockchain that can simulate real-world Ethereum transactions for development and testing purposes. You will need to run a local instance of Ganache to interact with the smart contract.

Running Ganache locally:
Install Ganache from Truffle Suite and open it.
The Ganache GUI will provide you with a local Ethereum blockchain, including a set of accounts with test ether.
The smart contract is deployed to this local instance of Ganache using the provided Web3 setup in the code.
Why the Ethereum blockchain can’t run on all PCs:

Resource Limitations: Running the Ethereum blockchain locally (via Ganache) can consume significant resources. Additionally, depending on your machine's hardware, running a local Ethereum node might require considerable processing power and memory.
Gas Fees Simulation: The smart contract uses Ethereum gas fees for interactions, which might be limited or simulated in Ganache. Real-world Ethereum networks require actual gas fees that cannot be simulated without using actual ether.
Ganache Limitation: For simulation purposes, the Ganache local network provides a lightweight version of the Ethereum blockchain but does not interact with the public Ethereum network. Therefore, for actual deployment and testing, a public testnet (e.g., Rinkeby) or the mainnet would be needed.

🔬 Quantum Models
Quantum Support Vector Machines (QSVM)
Variational Quantum Circuits (VQC)
Quantum Neural Networks (QNN)
🛡️ Federated Learning
Ensures data privacy using a distributed model training approach.
Collaborates across multiple organizations to improve fraud detection accuracy.
🔗 Blockchain Integration
Adds a layer of security and transparency.
Tracks data exchanges and ensures model integrity.
📂 Project Structure
bash
Αντιγραφή κώδικα
📂 Quantum-Fraud-Detection/
│
├── 📁 Code/        # Quantum model implementations, Blockchain integration scripts, Aggregation scripts, Cryptography & Hashing, Quantum Key Distribution
├── 📁 Datasets/            # 2 Datasets
├── 📁 Papers-Research/    # Federated learning models and orchestration
└── README.md                 # Project README

# Quantum Federated Learning for Fraud Detection

This project demonstrates the integration of **Quantum Federated Learning (QFL)** to solve the problem of fraud detection in financial systems. By combining **Quantum-inspired techniques** with **Federated Learning (FL)**, this solution enables decentralized model training while preserving privacy and enhancing security through quantum cryptography.

The project uses a **synthetic fraud detection dataset** and applies a variety of techniques such as **Quantum Neural Networks (QNN)**, **Homomorphic Encryption (HE)**, **Shamir’s Secret Sharing (SSS)**, and **blockchain** for aggregation to improve accuracy and privacy in fraud detection.

## Table of Contents
- [Project Overview](#project-overview)
- [Implementation Details](#implementation-details)
- [How to Run](#how-to-run)
- [Dependencies](#dependencies)
- [Results](#results)
- [Future Work](#future-work)
- [License](#license)

## Project Overview

The primary goal of this project is to use **Quantum Federated Learning (QFL)** for fraud detection across multiple financial institutions while maintaining data privacy and improving model performance. The project integrates **quantum computing** with **federated learning** techniques to enhance privacy-preserving machine learning.

### Key Features
- **Quantum Federated Learning**: Combines quantum techniques with federated learning for decentralized model training.
- **Privacy-Preserving**: Protects sensitive financial data using quantum cryptography and secure aggregation methods.
- **Adaptive Federated Learning**: Adjusts the weight contributions of clients based on their local model performance.
- **Homomorphic Encryption**: Ensures data privacy by encrypting client updates during the aggregation process.
- **Blockchain**: Uses blockchain technology to store aggregated model updates, ensuring integrity and transparency.

## Implementation Details

### Dataset Preparation
- The dataset used in this project is the **Synthetic Financial Fraud Dataset** for fraud detection. It is preprocessed using **Standard Scaling** and **SMOTE** (Synthetic Minority Over-sampling Technique) for class balancing.
- The dataset is split across multiple clients, with each client having a portion of the data to train their local model.

### Local Training
- Each client trains a **Quantum-enhanced model** locally on its dataset.
- The local models are trained using the **Keras** deep learning framework with a **Quantum Neural Network (QNN)** integrated using **PennyLane** for quantum-inspired layers.
- **Adaptive Federated Learning**: Clients with better local accuracy contribute more to the global model during aggregation, ensuring that high-performing clients have a larger influence on the global model.

### Secure Aggregation
- **Homomorphic Encryption (CKKS scheme)** is used to encrypt the updates during the federated aggregation process. This allows for secure aggregation of model updates without exposing the raw data.
- **Shamir’s Secret Sharing** is used to split the encrypted model weights, and **Qhashing** is employed to ensure the integrity of the aggregated model updates.
- Aggregated model updates are stored on a **blockchain** for transparency and security.

### Evaluation
- The model's performance is evaluated using **accuracy**, **precision**, **recall**, and **F1-score** on the **global test set** and each client's local test set.
- The evaluation ensures that clients contributing to the aggregation meet a performance threshold (adaptive federated learning).

## How to Run

### Prerequisites

- Python 3.7+
- Virtual environment (recommended)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/qfl-fraud-detection.git
   cd qfl-fraud-detection
 
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

3. Set up your local quantum simulator or hardware (if available):

Use PennyLane for quantum-inspired models and TensorFlow for the classical components.
Configure Web3 for blockchain integration and deploy the smart contract if you plan to use blockchain aggregation.

### Results
Client Performance: Each client trains a model locally with varying accuracies, which are aggregated into a global model. The performance of the global model is assessed based on client contributions.
Global Model Evaluation: After several iterations, the global model is evaluated on a combined test set from all clients.
The results of the global model's performance are stored and visualized over iterations, showing how the model improves through federated learning.

### Future Work
Real Quantum Hardware: The current implementation uses quantum simulators. Future work includes deploying the model on real quantum hardware to assess the impact of noise and coherence issues.
Blockchain Aggregation: Fully implement blockchain-based aggregation for real-world testing, ensuring secure and transparent model updates.
Scalability: Expand the system to handle larger datasets and more clients.
Advanced Quantum Algorithms: Explore advanced quantum algorithms for further optimization and enhancement of the fraud detection capabilities.

📬 Contact
For any questions or collaboration inquiries, please reach out to your email.
Epameinondas Douros -> epa.douros@gmail.com
Konstantinos Dalampekis -> konstantinosdalampekis@gmail.com

🔖 Acknowledgments
This project was supported by NYU Abu Dhabi and the Quantum Computing Research Lab.
