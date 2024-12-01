# Shamir’s Secret Sharing: Splitting weights
def shamir_split(secret, n, k, prime=PRIME):
    coeffs = [secret] + [random.randint(0, prime - 1) for _ in range(k - 1)]
    shares = [(i, sum(c * (i ** j) for j, c in enumerate(coeffs)) % prime) for i in range(1, n + 1)]
    return shares

# Encrypt weights with CKKS
def encrypt_weights(weights, context):
    encrypted_weights = []
    for weight in weights:
        flat_weights = weight.flatten().tolist()
        encrypted_vector = ts.ckks_vector(context, flat_weights)
        encrypted_weights.append(encrypted_vector)
    return encrypted_weights

# Define Qhash function
def qhash(data):
    """Generate a quantum-resistant hash (SHA-256) for the given data."""
    return sha256(data.encode()).hexdigest()
