import os
os.environ['CHROMA_DISABLE_DEFAULT_EMBEDDING'] = 'true'
os.environ['PYTHONNOUSERSITE'] = '1'

# Now import and run the main script
import sys
sys.path.append('/Users/georgesouza/Desktop/Python2025/Curriculo/resume_optimizer_crew_v2')
from src.crew import crew

# You can add any additional code to run the crew here
print('Crew created successfully!')
