# Define Qhash function
def qhash(data):
    """Generate a quantum-resistant hash (SHA-256) for the given data."""
    return sha256(data.encode()).hexdigest()

# Generate Qhash for encrypted weights
blockchain_batches = []  # To store batched Qhashes for blockchain

# Batch size for submission to blockchain
BATCH_SIZE = 10

print("Generating Qhashes and preparing batches for the blockchain...")
# Generate Qhash for encrypted weights


for batch_start in range(0, len(encrypted_shares), BATCH_SIZE):
    batch_end = min(batch_start + BATCH_SIZE, len(encrypted_shares))
    batch_hashes = []

    for node_id in range(batch_start, batch_end):
        # Flatten and serialize CKKS Vectors for Qhash
        serialized_shares = []
        for encrypted_weight in encrypted_shares[node_id]:
            if isinstance(encrypted_weight, ts.CKKSVector):  # Check for CKKSVector
                # Convert binary data to hexadecimal
                serialized_shares.append(encrypted_weight.serialize().hex())
            else:
                print(f"Skipping non-serializable object of type {type(encrypted_weight)}")

        serialized_shares_str = str(serialized_shares)
        hash_value = qhash(serialized_shares_str)  # Generate Qhash
        batch_hashes.append(hash_value)

    # Store the batch for blockchain submission
    blockchain_batches.append({
        "batch_start": batch_start,
        "batch_end": batch_end,
        "hashes": batch_hashes
    })

print(f"Prepared {len(blockchain_batches)} batches of Qhashes for blockchain submission.")


# Connect to Ethereum blockchain
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))  # Update with your provider

# Load smart contract ABI
with open('build/contracts/SecureAggregation.json') as f:
    contract_abi = json.load(f)["abi"]

# Contract address (update with your deployed contract address)
contract_address = "0xD1171913982F295a2172955E788c73fAD7aFcC06"

# Initialize smart contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Blockchain account for transactions
account = web3.eth.accounts[0]
web3.eth.default_account = account

# Submit Qhash batches to the blockchain
print("Submitting Qhash batches to the blockchain...")

for batch in blockchain_batches:
    try:
        # Convert Qhashes to bytes32 array
        batch_hashes_bytes = [bytes.fromhex(h) for h in batch["hashes"]]
        
        # Submit batch Qhashes to the smart contract
        tx = contract.functions.submitBatch(
            batch["batch_start"], batch["batch_end"], batch_hashes_bytes
        ).transact()
        
        # Wait for transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx)  # Corrected method
        print(f"Batch {batch['batch_start']} to {batch['batch_end']} submitted. Tx Hash: {receipt.transactionHash.hex()}")
    
    except Exception as e:
        print(f"Error submitting batch {batch['batch_start']} to {batch['batch_end']}: {e}")

print("All Qhash batches successfully submitted to the blockchain.")


def trust_based_weighting(factors, reputation_scores):
    """
    Adjust adaptive factors based on client reputation scores.
    Higher reputation -> higher weight in aggregation.
    """
    adjusted_factors = [f * reputation_scores[i] for i, f in enumerate(factors)]
    total_factor = sum(adjusted_factors)
    
    # Normalize to keep total sum as 1
    return [f / total_factor for f in adjusted_factors]

def filter_outliers(encrypted_shares, threshold=2.0):
    """
    Filter out model updates that deviate significantly from the mean.
    """
    decrypted_values = [np.array(weights.decrypt()) for weights in encrypted_shares]
    mean_values = np.mean(decrypted_values, axis=0)
    std_dev = np.std(decrypted_values, axis=0)

    # Identify outliers
    filtered_updates = []
    for weights in decrypted_values:
        deviation = np.abs(weights - mean_values) / (std_dev + 1e-6)
        if np.max(deviation) < threshold:
            filtered_updates.append(weights)

    return filtered_updates

def median_aggregator_qnn_parameters(encrypted_params, factors, reputation_scores):
    """
    Perform weighted median aggregation with trust-based weighting.
    """
    weights = trust_based_weighting(factors, reputation_scores)
    num_layers = len(encrypted_params[0])  # Assuming all clients have the same layer structure
    aggregated_params = []
    
    for layer_idx in range(num_layers):
        layer_params = [client[layer_idx] for client in encrypted_params]
        layer_stack = np.array([param.decrypt() for param in layer_params])  # Decrypt if needed
        
        median_layer = np.zeros_like(layer_stack[0])
        for param_idx in range(layer_stack.shape[1]):  # Assuming 1D parameter arrays
            param_values = layer_stack[:, param_idx]
            sorted_indices = np.argsort(param_values)
            sorted_values = param_values[sorted_indices]
            sorted_weights = np.array(weights)[sorted_indices]
            
            cumulative_weights = np.cumsum(sorted_weights)
            median_index = np.searchsorted(cumulative_weights, 0.5)
            median_layer[param_idx] = sorted_values[median_index]
        
        aggregated_params.append(median_layer)  # Optionally re-encrypt if needed
    
    return aggregated_params

def get_reputation_scores_from_blockchain():
    """
    Retrieve client reputation scores from the blockchain.
    """
    reputation_scores = {}
    for client_id in range(NUM_CLIENTS):
        client_address = web3.eth.accounts[client_id]
        score = contract.functions.reputationScores(client_address).call()
        reputation_scores[client_id] = score if score > 0 else 1  # Avoid zero scores
    return reputation_scores


# Example : # Fetch reputation scores from blockchain
# reputation_scores = get_reputation_scores_from_blockchain()

# # Generate adaptive factors
# adaptive_factors = generate_adaptive_factors(NUM_CLIENTS)

# # Adjust weights based on reputation
# adjusted_factors = trust_based_weighting(adaptive_factors, reputation_scores)

# # Filter outliers before aggregation
# valid_updates = filter_outliers(encrypted_shares)

# # Perform trust-weighted aggregation
# aggregated_encrypted_weights = median_aggregator_qnn_parameters(valid_updates, adjusted_factors, reputation_scores)
