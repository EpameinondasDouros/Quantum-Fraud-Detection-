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
   ```bash
      📂 Quantum-Fraud-Detection/
      │
      ├── 📁 Code/        # Quantum model implementations, Blockchain integration scripts, Aggregation scripts, Cryptography & Hashing, Quantum Key Distribution
      ├── 📁 Datasets/            # 2 Datasets
      ├── 📁 Papers-Research/    # Federated learning models and orchestration
      └── README.md                 # Project README
```      
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

# Quantum Federated Learning for Fraud Detection

## Implementation

### Technologies Used

#### Quantum Federated Learning (QFL):
- **PennyLane**: This Python library provides the necessary tools for creating quantum circuits and quantum neural networks (QNNs). It is used to implement quantum-enhanced models at each client node. PennyLane enables hybrid quantum-classical learning and allows us to simulate quantum computations for training and evaluating the fraud detection model.

#### Machine Learning:
- **TensorFlow/Keras**: These libraries were used to implement the classical parts of the model, particularly the layers, optimization, and evaluation of the neural networks. TensorFlow/Keras provides the necessary framework for training the models locally on each client’s dataset.

#### Homomorphic Encryption:
- **TenSEAL**: A library for performing homomorphic encryption (HE), allowing encrypted data to be processed and aggregated securely. It ensures that client data remains private during training and aggregation.
- **Shamir's Secret Sharing**: This cryptographic technique was used to split and share model weights among clients in a way that prevents any single client from accessing the entire model's parameters.

#### Blockchain:
- **Ethereum (via Web3)**: A smart contract was deployed to an Ethereum test network (simulated using Ganache) to store and verify the integrity of model weights using a secure, transparent blockchain system. The blockchain ensures that all model updates are recorded and tamper-proof, ensuring model integrity.

#### Quantum Key Distribution (QKD):
- **QKD Simulation**: To ensure that model weights and updates are securely transmitted between the clients during the federated learning process, Quantum Key Distribution (QKD) was simulated. QKD allows for the secure exchange of encryption keys over potentially insecure channels, ensuring that the client models' updates are encrypted using keys that have been securely shared. In this project, QKD was simulated to manage the secure encryption of model weights, which would otherwise be vulnerable to interception in classical federated learning.

#### Synthetic Data Generation:
- **SMOTE (Synthetic Minority Oversampling Technique)**: SMOTE was used to balance the dataset by generating synthetic fraud cases. This ensures that the training dataset for each client is representative and that the model does not suffer from data imbalance issues.

---

### Adaptive Federated Learning Process

The **Adaptive Federated Learning** approach used in this project focuses on selectively aggregating model updates from clients based on their performance, and it adapts the contribution of each client during the aggregation process. Below is a breakdown of the process:

#### Client-Side Training:
- Each client in the federated network trains its local model using its own data, which may be a subset of the overall dataset. The local models are enhanced by quantum-inspired layers (QNNs) and classical neural network layers.
- Clients train their models independently on their local datasets, which are securely encrypted using homomorphic encryption, ensuring that sensitive data is never shared or exposed.

#### Adaptive Client Selection:
- Before aggregating the model updates, the global model's performance on each client’s local test set is evaluated. Clients that perform well locally are selected for the aggregation process.
- The performance threshold is set based on the accuracy on each client’s local test set. Clients whose accuracy falls below the threshold are excluded from the aggregation to avoid negatively affecting the global model's performance.
- Clients above the threshold are selected to contribute their model updates to the global model.

#### Weighted Aggregation:
- The selected clients contribute their model updates, but the aggregation is not performed equally. Instead, each client’s contribution is weighted based on its local performance, specifically its accuracy.
- A weighted average aggregation method is applied, where each client’s model update is scaled according to its accuracy. This ensures that clients with better performance on their local test sets have a stronger influence on the global model.

#### Secure Model Update and Encryption:
- Model weights are encrypted using homomorphic encryption to maintain the privacy of the clients' updates. Shamir's Secret Sharing is used to split the weights and share them securely among the clients, ensuring no client has full access to the model parameters.
- **QKD (Quantum Key Distribution)** is simulated to securely exchange encryption keys between clients, further enhancing the security of the model updates during transmission.

#### Blockchain Integrity Check:
- After aggregation, the global model's updated weights are hashed using **Qhash**, a quantum-resistant hashing technique, and stored on a blockchain. This step ensures the integrity and authenticity of the global model and prevents tampering with the weights.
- The blockchain provides a transparent and immutable record of all model updates and serves as a decentralized ledger for verifying the aggregated updates.

#### Global Model Update:
- The aggregated weights are decrypted and used to update the global model. The global model is then redistributed back to the clients for the next round of training.
- By using this adaptive federated learning method, the model continuously improves over multiple iterations without compromising the privacy of the clients' data.

## How to Run

### Prerequisites

- Python 3.7+
- Virtual environment (recommended)
- Tensorflow 2.10.0

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/EpameinondasDouros/Quantum-Fraud-Detection-.git  

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

### Model Performance Comparison

| Model           | Dataset      | Accuracy (%) | 
|-----------------|--------------|--------------|                
| Client 0        | 99.45        |              |
| Client 1        | 86.47        |              |      
| Client 2        | 74.92        |              |
| Client 3        | 83.14        |              |
| Client 4        | 92.86        |              |
| Client 5        | 75.90        |              |
| Client 6        | 89.52        |              |
| Client 7        | 85.17        |              |
| Client 8        | 85.77        |              |
| Client 9        | 91.37        |              |

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
