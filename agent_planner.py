# agent_planner.py
import subprocess

def plan_agent_response(prompt: str):
    command = ["ollama", "run", "tinyllama", f"Give clothing planning suggestions: {prompt}"]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()
