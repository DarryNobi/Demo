import numpy as np
import json
import os
from web.models import AutoGraphicLabel

def load_jsons(path):
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.json':
            file = os.path.join(path, file)
            with open(file, 'r') as load_f:
                load_dict = json.load(load_f)
            for graphic_dict in load_dict:
                graphictype=graphic_dict['properties']
                graphic = AutoGraphicLabel.objects.create(context=json.dumps(graphic_dict),graphictype=graphictype['type'])
                graphic.save()
    return 0


def main():
    mybasepath='./Maps/49'
    load_jsons(mybasepath)
    return 0


if __name__=='__main__':
    main()