import subprocess
import json
import sys

def run_node_script(input_text):
    # Replace the path to your Node.js script if necessary
    result = subprocess.run(['node', 'C:/KaliAIMailer/3rd Party Model/geminiApiAccess.js', input_text], capture_output=True, text=True)
    if result.stderr:
        print("Error:", result.stderr, file=sys.stderr)
    else:
        print("Output:", result.stdout)

if __name__ == "__main__":
    user_input = input("Enter your input for the AI: ")
    run_node_script(user_input)
