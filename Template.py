#setting up the libraries
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

#providing the project_name
project_name = 'TextSummarizer'

#creating the list of files and folders required for the project

list_of_files = [
    '.github/workflows/.gitkeep', #creating an empty file later on it will be deleted
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml', # parameters for the ml model
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trails.ipynb'
]

for filepath in list_of_files:
    filepath = Path(filepath) #path function helps to identify the path of the file/folder regardless windows/linux
    filedir, filename = os.path.split(filepath) #path.split splits the folder and filenames

    #folder creation and checking if the fildir is not empty
    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'creating directory:{filedir} for the file {filename}')
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #when the file size is empty
        with open(filepath,'w') as f:
            pass
            logging.info(f'Creating empty file: {filepath}')
    else:
        logging.info(f'{filename} is already exists')




