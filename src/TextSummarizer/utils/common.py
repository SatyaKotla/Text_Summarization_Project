#creating the utilities required for the project
#the functions which are used regularly throught the project
#setting up the  libraries
import os
from box.exceptions import BoxValueError
import yaml
from TextSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

#creating read_yaml function

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        Value Error : if yaml file is empty
        e : if empty file
    
    Returns:
        ConfigBox : configBox Type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded succesfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

#creating create_directories function
@ensure_annotations
def create_directories(path_to_directories: list,verbose= True):
    '''Create list of directories
    Args:
        path_to_directories(list): list of path to directories
        ignore_log(bool, optional): ignore if multiple directories are to be created. Defaults to False

    '''

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'created directory at: {path}')

#creating get_size function
@ensure_annotations
def get_size(path: Path) -> str:
    '''get size in KB

    Args:
        path(Path): path of the file
    
    Returns:
        str: size in KB
    '''
    size_in_kb = round(os.path.getsize(path)/1024)
    return(f'~{size_in_kb} KB')

