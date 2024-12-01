def decrypt_with_aes(encrypted_model, key):
    """Decrypt the encrypted global model using the AES key."""
    if len(key) not in {16, 24, 32}:
        raise ValueError("Invalid AES key length. Must be 16, 24, or 32 bytes.")

    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt all blocks
    decrypted_bytes = b"".join([decryptor.update(block) for block in encrypted_model])

    # Remove PKCS7 padding
    unpadder = padding.PKCS7(128).unpadder()
    plaintext_bytes = unpadder.update(decrypted_bytes) + unpadder.finalize()

    # Unpack floats
    decrypted_weights = [struct.unpack("!f", plaintext_bytes[i:i + 4])[0] for i in range(0, len(plaintext_bytes), 4)]
    return decrypted_weights

def deserialize_model_weights(serialized_weights, model):
    """Reshape serialized weights and biases back to their original shapes."""
    deserialized_weights = []
    start = 0
    for layer in model.layers:
        if hasattr(layer, "get_weights"):
            weights = layer.get_weights()
            if len(weights) == 2:  # Both weights and biases
                weight_shape = weights[0].shape
                bias_shape = weights[1].shape

                weight_count = np.prod(weight_shape)
                bias_count = np.prod(bias_shape)

                weights = np.array(serialized_weights[start:start + weight_count]).reshape(weight_shape)
                biases = np.array(serialized_weights[start + weight_count:start + weight_count + bias_count]).reshape(bias_shape)

                deserialized_weights.append((weights, biases))
                start += weight_count + bias_count
            elif len(weights) == 1:  # Only weights
                weight_shape = weights[0].shape
                weight_count = np.prod(weight_shape)

                weights = np.array(serialized_weights[start:start + weight_count]).reshape(weight_shape)
                deserialized_weights.append((weights, None))
                start += weight_count
    return deserialized_weights
