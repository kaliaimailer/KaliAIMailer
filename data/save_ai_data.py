# Import the pickle module
import pickle

# Define some AI data to save
# For example, this could be the output of a machine learning model training process
ai_data = {
    'model_name': 'SampleModel',
    'accuracy': 0.95,
    'parameters': {'learning_rate': 0.01, 'epochs': 100},
}

# Specify the path to the file where you want to save the data
file_path = 'data/ai_data.pkl'

# Use the 'with' statement to ensure the file is properly closed after writing
with open(file_path, 'wb') as file:
    # Use pickle.dump() to serialize the ai_data and save it to the file
    pickle.dump(ai_data, file)

print(f'AI data has been saved to {file_path}')
