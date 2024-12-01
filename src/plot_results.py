# Plot evaluation results
plt.figure(figsize=(10, 6))
plt.plot(range(1, ITERATIONS + 1), evaluation_results_global, marker='o')
plt.title('Global Model Accuracy Over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Accuracy (%)')
plt.grid()
plt.show()

# Plot evaluation results
plt.figure(figsize=(10, 6))
plt.plot(range(1, ITERATIONS + 1), evaluation_results_local, marker='o')
plt.title('Local Model Accuracy Over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Accuracy (%)')
plt.grid()
plt.show()
