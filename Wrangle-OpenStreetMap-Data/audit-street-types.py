import re
from collections import defaultdict
import xml.etree.cElementTree as ET


def v_attrib_types(filename, k_attrib_value, pattern, expected):
    '''
    This function will seperate the k attribute value based on their patterns
    within a .osm file.

    Parameters
    ---
    filename (.xml or .osm): The file that is going to be parsed.
    k_attrib_value (str): The k attribute value you are looking for.
    pattern (re): The regex pattern used to categorize the k attribute value
    expected (list or re): the expected value list or pattern

    Return
    ---
    A dictionary conatains the category of the k values.
    '''
    types = defaultdict(set)

    for event, element in ET.iterparse(filename, events=('start',)):
        if element.tag == 'node' or element.tag == 'way':
            for tag in element.iter('tag'):
                if tag.attrib['k'] == k_attrib_value:
                    v_value = tag.attrib['v']
                    search = pattern.search(v_value)
                    if search:
                        v_type = search.group(0)
                        try:
                            if v_type not in expected:
                                types[v_type].add(v_value)
                        except:
                            if not expected.search(v_type):
                                types[v_type].add(v_value)

    return types