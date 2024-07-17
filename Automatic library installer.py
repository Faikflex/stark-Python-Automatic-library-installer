import subprocess
import sys

def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"{package_name} başarıyla yüklendi.")
    except subprocess.CalledProcessError as e:
        print(f"{package_name} yüklenirken bir hata oluştu: {e}")

if __name__ == "__main__":
    package_name = input("Lütfen yüklemek istediğiniz Python kütüphanesinin ismini girin: ")
    install_package(package_name)