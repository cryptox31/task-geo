"""
Datapackager will create a datapackge.json file with the provided dataset file
"""
import json
import os

from datapackage import Package


def datapackage_creater(path_to_dataset_file, metadata, keywords):
    """Creates a datapackage.json file

    Args:
        path_to_dataset_file (pandas.DataFrame): dataset returned by an api
        metadata (dict): Dictionary containing metadata
        Examples:
        >>> { 'name' : '', \
              'description': '', \
              'url': '', \
            }
        keywords (list<str>): List of keywords
        Examples
        >>> ['covid19', 'coronavirus']
    """
    keyword_dict = {'keywords': keywords}
    metadata_dict = {'id': '', 'size': os.path.getsize(path_to_dataset_file),
                     'data_source_revision_last_updated': metadata['revision_last_updated'],
                     'data_source_last_modified': metadata['last_modified'],
                     'data_source_created': metadata['created'],
                     'description': metadata['description'], 'name': metadata['name'],
                     'url': metadata['url'], 'download_url': metadata['download_url']}
    package = Package()
    package.infer(path_to_dataset_file)
    package.save('datapackage.json')
    with open('datapackage.json') as json_file:
        data = json.load(json_file)
    data.update(metadata_dict)
    data.update(keyword_dict)
    with open('datapackage.json', 'w') as f:
        json.dump(data, f, indent=4)
