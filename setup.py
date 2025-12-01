import email
from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requiremnets:
    '''
    requirements=[]
    hyphon_dot='-e .'
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if hyphon_dot in requirements:
            requirements.remove(hyphon_dot)
    return requirements

setup(
    name='LLM END TO END PROJECT',
    version='0.0.1',
    author='Shahbaz Khan',
    author_email='skhan0827779@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)