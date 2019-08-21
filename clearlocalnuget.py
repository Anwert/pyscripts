import os

NUGET_PATH = r'C:\LocalNuget'


for item in os.listdir(NUGET_PATH):
    os.remove(NUGET_PATH + r'\\' + item)

print("Local nuget was cleared")