# -*- coding: utf-8 -*-
## http://pyyaml.org/wiki/PyYAMLDocumentation
## pip install pyaml


import yaml


# def represent_ordereddict(dumper, data):
#     value = []
#
#     for item_key, item_value in data.items():
#         node_key = dumper.represent_data(item_key)
#         node_value = dumper.represent_data(item_value)
#         value.append((node_key, node_value))
#
#     return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)
#
#
# yaml.add_representer(OrderedDict, represent_ordereddict)

with open('yml_sample.yml', 'r') as f:
    result = yaml.load(f)
    print(result)
    print(type(result))
    result['yaml_key1'] = 'yaml_value_changed'

with open('yml_dump.yml', 'w') as f:
    yaml.dump(result, f, allow_unicode=True, default_flow_style=False)
