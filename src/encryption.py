for iteration in range(ITERATIONS):
    print(f"\n--- Iteration {iteration + 1} ---")
    

    for client_id, (X_train, X_test, y_train, y_test) in enumerate(client_splits):
    # for client_id, client_data in enumerate(client_dfs):
        print(f"Training quantum model for Client {client_id + 1}")
        
        # Preprocess client data
        X_client = X_train
        y_client = y_train

        
        # Fit the model with verbose=1 to display training progress
        client_models[client_id].fit(X_client, y_client, batch_size=32, epochs=3, verbose=1)
    
    client_global_performances = []
    selected_clients = []  # Ensure the list is reset for each iteration

    threshold = 80  # Minimum accuracy required to contribute
    if iteration >= 1:
        for client_id, (X_train_l, X_test_l, y_train_l, y_test_l) in enumerate(client_splits):
            # Evaluate global model's performance on each client's test set
            accuracy_local = evaluate_model(global_model, X_test_l, y_test_l)
            client_global_performances.append(accuracy_local)
            
            # Print performance for each client
            print(f"Client {client_id}: Accuracy on its test set = {accuracy_local:.2f}%")
            
            # Add client to the selected list if accuracy meets the threshold
            if accuracy_local >= threshold:
                selected_clients.append(client_id)

        # Print the list of selected clients
        print(f"Selected clients for aggregation: {selected_clients}")

    # Initialize CKKS Context for Homomorphic Encryption
    context = ts.context(
        ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 40, 60]
    )
    context.global_scale = 2 ** 40

    print("CKKS Context initialized.")

    

    # Process and secure weights from client models
    # Encrypt weights after training
    encrypted_shares = []
    for client_id, model in enumerate(client_models):
        print(f"Securing weights for Client {client_id + 1}")

        # Extract weights from the trained model
        weights = [layer.get_weights()[0] for layer in model.layers if isinstance(layer, Dense)]

        # Shamir's Secret Sharing (already in place)
        node_shares = []
        for weight_matrix in weights:
            shares = [
                shamir_split(int(value * 1e6), NUM_NODES, THRESHOLD, PRIME)
                for value in weight_matrix.flatten()
            ]
            node_shares.append(shares)

        # CKKS encryption
        encrypted_weights = encrypt_weights(weights, context)

        encrypted_shares.append(encrypted_weights)
        print(f"Client {client_id + 1}: Weights encrypted and secured.")
