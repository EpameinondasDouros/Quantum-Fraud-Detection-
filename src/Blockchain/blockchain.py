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
