from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    
    # Removing any extra spaces and new line characters
    requirements = [req.replace('\n', '').strip() for req in requirements]
    
    # If '-e .' is present, remove it
    if '-e .' in requirements:
        requirements.remove('-e .')
    
    return requirements

setup(
    name='ML-project',version='0.0.1',
    author='Nandini Vashista',
    author_email='vashistanandini@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)