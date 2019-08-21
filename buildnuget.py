import shutil, os

NUGET_PATH = r'C:\LocalNuget'
NUGET_CACHE_PATH = r'C:\Users\krutakov.fedor\.nuget\packages'


# выполняет переданную функцию для .nupkg файлов в директории bin
def do_with_nupkg(bin, function, *args):
    for item in os.listdir(bin):
        if item.endswith('.nupkg'):
            function(os.path.join(bin, item), *args)

# записываем путь, откуда вызывается скрипт и формируем название пакета на основе пути
proj_path = os.getcwd()
package_name = "cordis." + os.path.basename(proj_path)

# проверяем, что путь до проекта существует
proj_path = proj_path + r'\\' + package_name
if not os.path.exists(proj_path):
    raise Exception("Путь до проекта не найден.")

# чистим кеш
cache_path = NUGET_CACHE_PATH + r'\\' + package_name
if os.path.exists(cache_path):
    shutil.rmtree(cache_path)

bin = proj_path + r'\bin\Release'

# удаляем все старые сбилженные файлы .nupkg
if os.path.exists(bin):
    do_with_nupkg(bin, os.remove)

# билдим пакет
os.system("dotnet build -c:Release -v:q " + proj_path)

# копируем сбилженные файлы .nupkg в нужную папку
do_with_nupkg(bin, shutil.copy2, NUGET_PATH)