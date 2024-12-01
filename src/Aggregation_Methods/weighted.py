# Generate adaptive factors for each client
def generate_adaptive_factors(num_clients, lower=0.5, upper=1.5):
    """Generate random adaptive factors for clients within a specified range."""
    factors = [random.uniform(lower, upper) for _ in range(num_clients)]
    return factors

# Perform weighted average aggregation
def weighted_average_ckks_nested(encrypted_weights, factors):
    """Perform weighted average aggregation on nested CKKS-encrypted weights."""
    total_factor = sum(factors)
    aggregated_weights = []

    for layer_idx in range(len(encrypted_weights[0])):
        aggregated_layer = encrypted_weights[0][layer_idx].copy()
        for i, client_weights in enumerate(encrypted_weights[1:], start=1):
            aggregated_layer += client_weights[layer_idx] * (factors[i] / total_factor)
            aggregated_weights.append(aggregated_layer)

    # Log size of each layer's aggregated weights
    for idx, layer in enumerate(aggregated_weights):
        print(f"Layer {idx}: Aggregated weights size = {len(layer.decrypt())}")
        return aggregated_weights
    
    
    
# Define Qhash function
def qhash(data):
    """Generate a quantum-resistant hash (SHA-256) for the given data."""
    return sha256(data.encode()).hexdigest()

# Convert the aggregated Qhash to bytes32
def str_to_bytes32(input_str):
    """Convert a string to bytes32."""
    return bytes.fromhex(input_str)
