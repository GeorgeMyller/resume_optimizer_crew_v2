#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv
from crew import ResumeOptimizerCrew

def run():
    load_dotenv()
    # Substitua pelos seus inputs reais
    inputs = {
        'resume_path': 'src/input',
        'job_url': 'https://jobs.foundever.com/job/Porto-Data-Analyst-Porto%2C-Portugal-Port/1278591600/?utm_source=LINKEDIN&utm_medium=referrer'
    }
    result = ResumeOptimizerCrew().crew().kickoff(inputs=inputs)
    print("\n✅ Crew finished execution.")
    print("\n📄 Generated Resume Content:")
    print(result)
    # Salvar resultado em arquivo
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "novo_curriculo.tex")
    with open(output_path, "w", encoding='utf-8') as f:
        f.write(str(result))
    print(f"\n💾 Optimized resume saved to: {output_path}")

if __name__ == "__main__":
    run()
