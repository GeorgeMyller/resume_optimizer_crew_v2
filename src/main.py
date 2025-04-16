'''
This is the main module that runs the resume optimization crew.
It loads environment variables, configures the crew, and kicks off the optimization process.
'''
import os
import sys
import argparse
from datetime import datetime
from .crew import resume_optimizer_crew # Changed from 'from src.crew import crew'
from dotenv import load_dotenv

# Load environment variables from .env file

# Load variables from .env file
load_dotenv()

# Check if required environment variables exist
if not os.environ.get("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY not found in .env file")

if not os.environ.get("OPENAI_API_BASE"):
    # Set default API base if not provided
    os.environ["OPENAI_API_BASE"] = "https://generativelanguage.googleapis.com/v1beta"
    
if not os.environ.get("OPENAI_MODEL_NAME"):
    # Set default model if not provided
    os.environ["OPENAI_MODEL_NAME"] = "gemini-2.0-flash"

def generate_unique_filename(base_name="output", extension=".tex"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}{extension}"

if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Run the Resume Optimizer Crew.')
    parser.add_argument('--resume', type=str, required=True, help='Path to the resume .tex file.')
    parser.add_argument('--job-url', type=str, required=True, help='URL of the job description.')
    parser.add_argument('--output-dir', type=str, default='output', help='Directory to save the optimized resume.')

    # Parse arguments
    args = parser.parse_args()

    # Define inputs for the crew
    inputs = {
        'resume_path': args.resume,
        'job_url': args.job_url
    }
    
    print("\n🚀 Kicking off the Crew...")
    result = resume_optimizer_crew.kickoff(inputs=inputs) # Use the imported name
    
    print("\n✅ Crew finished execution.")
    print("\n📄 Generated Resume Content:")
    print(result) # Print the actual result
    
    # Ensure output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    unique_filename = generate_unique_filename(base_name="optimized_resume")
    output_path = os.path.join(output_dir, unique_filename)
    
    # Save the actual result to the file
    try:
        with open(output_path, "w", encoding='utf-8') as output_file:
            output_file.write(result) # Save the actual result
        print(f"\n💾 Optimized resume saved to: {output_path}")
    except Exception as e:
        print(f"\n❌ Error saving file: {e}")
