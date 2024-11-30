
This folder contains the datasets used for training and evaluating the Quantum Federated Learning (QFL) fraud detection model.

## Datasets

### 1. Fraud Detection Bank Dataset
- **Description**: A dataset containing transactions with labeled fraudulent and non-fraudulent entries, used to train the fraud detection models.
- **Source**: [Link to dataset](https://www.kaggle.com/datasets/volodymyrgavrysh/fraud-detection-bank-dataset-20k-records-binary)
- **Columns**: 
  - `targets`: Labels indicating fraudulent transactions (0 for non-fraudulent, 1 for fraudulent).

### 2. Synthetic Financial Fraud Dataset (Optional)
- **Description**: A synthetic dataset used for simulating fraud detection in a controlled environment. This dataset is generated to balance the classes and simulate more realistic fraud cases.
- **Source**: [Link to dataset](https://www.kaggle.com/datasets/ealaxi/paysim1)
- **Columns**: 
  - `targets`: Labels indicating fraudulent transactions (0 for non-fraudulent, 1 for fraudulent).

## Data Preprocessing

- **SMOTE (Synthetic Minority Over-sampling Technique)**: Used for balancing the dataset by generating synthetic fraud cases to prevent the model from being biased towards the majority class.
- **Feature Scaling**: The features in the dataset were scaled using `StandardScaler` to ensure that all features contribute equally to the model training.
- **Data Split**: The dataset is split into training and testing sets using `train_test_split` to evaluate the model's performance.

## How to Use

To use the datasets in this folder:
1. Clone this repository to your local machine.
2. Access the dataset files inside the `dataset/` folder.
3. Load the dataset into your Python environment using `pandas` (e.g., `pd.read_csv('dataset/fraud_detection_bank_dataset.csv')`).
4. Use the data as input for training the Quantum Federated Learning model.


