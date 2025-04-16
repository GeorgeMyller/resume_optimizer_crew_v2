#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv
from crew import ResumeOptimizerCrew

def run():
    load_dotenv()
    # Inputs corrigidos e prints de depuração
    resume_path = 'input/curriculo.tex'  # Caminho corrigido
    job_url = 'https://jobs.foundever.com/job/Porto-Data-Analyst-Porto%2C-Portugal-Port/1278591600/?utm_source=LINKEDIN&utm_medium=referrer'
    print(f"[DEBUG] Usando resume_path: {resume_path}")
    print(f"[DEBUG] Usando job_url: {job_url}")
    inputs = {
        'resume_path': resume_path,
        'job_url': job_url
    }
    try:
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
    except Exception as e:
        print(f"[ERRO] Ocorreu uma exceção: {e}")

if __name__ == "__main__":
    run()
