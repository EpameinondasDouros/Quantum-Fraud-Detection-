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


    
    # Generate adaptive factors
    adaptive_factors = generate_adaptive_factors(NUM_CLIENTS)
    
    if iteration >= 1:
            # Aggregate only from selected clients
        selected_encrypted_weights = [encrypted_shares[client_id] for client_id in selected_clients]
        selected_factors = [adaptive_factors[client_id] for client_id in selected_clients]

        # Print selected clients for transparency
        print(f"Selected clients contributing to aggregation: {selected_clients}")
        
        # Perform weighted aggregation
        aggregated_encrypted_weights = median_aggregator_qnn_parameters(selected_encrypted_weights, selected_factors)
    else:
            # Perform adaptive weighted aggregation on encrypted weights
        print("Aggregating encrypted weights using adaptive weighted CKKS aggregation...")
        try:
            aggregated_encrypted_weights = median_aggregator_qnn_parameters(encrypted_shares, adaptive_factors)
            print("Encrypted weights aggregated successfully.")
        except Exception as e:
            print(f"Error during adaptive aggregation: {e}")
