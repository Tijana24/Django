with open('newfile.txt','w') as file_object:
    file_object.writelines('Test')

import json

print(json.dumps(['Welcome', "to", 'GeekforGeeks']))