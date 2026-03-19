import subprocess
import os

def get_ai_fix():
    # 1. We assume the test failure log was saved to 'failure.log' by the pipeline
    if not os.path.exists("failure.log"):
        return "No failure log found."

    with open("failure.log", "r") as f:
        error_content = f.read()[-1000:] # Get the last 1000 characters (the crash)

    # 2. Call the GitHub Copilot CLI to explain the error
    # The '-p' flag runs Copilot in 'Programmatic Mode' for automation
    prompt = f"The following Python unit test failed. Explain the root cause and provide a code fix:\n\n{error_content}"
    
    try:
        result = subprocess.run(
            ["copilot", "-p", prompt],
            capture_output=True,
            text=True,
            env=os.environ # Pass the COPILOT_GITHUB_TOKEN from the env
        )
        return result.stdout
    except Exception as e:
        return f"AI Diagnosis failed: {str(e)}"

if __name__ == "__main__":
    print("--- AI ROOT CAUSE ANALYSIS ---")
    print(get_ai_fix())
