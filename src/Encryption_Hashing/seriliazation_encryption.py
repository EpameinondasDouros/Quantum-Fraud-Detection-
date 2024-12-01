def serialize_model_weights(model):
        """Flatten weights and biases for all layers into a single list."""
        serialized_weights = []
        for layer in model.layers:
            if hasattr(layer, "get_weights"):
                weights = layer.get_weights()
                if len(weights) == 2:  # If both weights and biases exist
                    serialized_weights.extend(weights[0].flatten())  # Flatten weights
                    serialized_weights.extend(weights[1].flatten())  # Flatten biases
                elif len(weights) == 1:  # If only weights exist (no biases)
                    serialized_weights.extend(weights[0].flatten())
                else:
                    print(f"Layer {layer.name} has no trainable weights or biases.")
        return [struct.pack("!f", w) for w in serialized_weights]  # Convert to bytes


def encrypt_with_aes(plaintext_weights, key):
    """Encrypt the plaintext weights using AES key."""
    if len(key) not in {16, 24, 32}:
        raise ValueError("Invalid AES key length. Must be 16, 24, or 32 bytes.")

    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # Convert list of packed floats to a single byte string
    plaintext_bytes = b"".join(plaintext_weights)

    # PKCS7 padding to align plaintext with AES block size
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext_bytes) + padder.finalize()

    # Encrypt in blocks
    encrypted_weights = []
    for i in range(0, len(padded_data), 16):
        block = padded_data[i:i + 16]
        encrypted_weights.append(encryptor.update(block))

    return encrypted_weights

def simulate_qkd_resources(num_nodes):
    """Simulate QKD key generation for secure model redistribution."""
    return {node_id: {"key": os.urandom(16)} for node_id in range(num_nodes)}
