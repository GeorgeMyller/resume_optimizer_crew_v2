#!/usr/bin/env python
import sys
from matchcv.crew import MatchcvCrew

def run():
    # Substitua pelos seus inputs, ele irá interpolar automaticamente qualquer informação de tarefas e agentes
    inputs = {
        'path_to_jobs_csv': './src/matchcv/data/jobs.csv',
        'path_to_cv': './src/matchcv/data/cv.md',
        'path_to_new_cv': './src/matchcv/data/new_cv.md'
    }
    MatchcvCrew().crew().kickoff(inputs=inputs)

