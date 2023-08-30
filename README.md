# python_tkinter

hello
python3.10.12 설
sudo apt install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev


wget https://www.python.org/ftp/python/X.Y.Z/Python-X.Y.Z.tgz

tar -xf Python-X.Y.Z.tgz

cd Python-X.Y.Z

./configure --enable-optimizations

make -j$(nproc)

sudo make altinstall

python3.10 --version



