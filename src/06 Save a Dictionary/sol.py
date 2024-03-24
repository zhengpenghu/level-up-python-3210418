import json


def save_dict(dict, output_path):
    with open(output_path, 'w') as file:
        file.write(json.dumps(dict))


def load_dict(dict_path):
    with open(dict_path, 'r') as file:
        d = json.load(file)
    return d


if __name__ == '__main__':
    save_dict({1: 'a', 2: 'b', 3: 'c'}, 'test.pickle')
    print(load_dict('test.pickle'))
    # {1: 'a', 2: 'b', 3: 'c'}
