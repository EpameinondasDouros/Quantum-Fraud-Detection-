# Function to evaluate model on the test set
def evaluate_model(global_model, X_test, y_test):
    """
    Evaluate the global model's accuracy on the test dataset.
    """
    y_pred = global_model.predict(X_test)
    y_pred_classes = np.argmax(y_pred, axis=1)
    accuracy = np.mean(y_pred_classes == y_test) * 100
    return accuracy

    # Evaluate the global model on the test set
    global_model = client_models[0]  # Assuming all models are synced to the same global weights
    
    X_train_0, X_test_0, y_train_0, y_test_0 = client_splits[0]

    global_model=client_models[0]
    
    
    # Evaluate the global model on combined test set
    X_global_test = np.vstack([X_test for _, X_test, _, _ in client_splits])
    y_global_test = np.hstack([y_test for _, _, _, y_test in client_splits])
    accuracy_global = evaluate_model(global_model, X_global_test, y_global_test)

    # Evaluate the first client's model on its own test set
    accuracy_local_1 = evaluate_model(client_models[0], X_test_0, y_test_0)

    print(f"Iteration {iteration + 1}: Global model accuracy on combined test set = {accuracy_global:.2f}%")
    print(f"Iteration {iteration + 1}: Client 1 model accuracy on its own test set = {accuracy_local_1:.2f}%")

    evaluation_results_global.append(accuracy_global)
    evaluation_results_local.append(accuracy_local_1)
        
    for i in range(len(client_splits)):
        X_train, X_test, y_train, y_test = client_splits[i]
        accuracy_local = evaluate_model(global_model, X_test, y_test)
        print(f"Client {i}: Accuracy = {accuracy_local}")
