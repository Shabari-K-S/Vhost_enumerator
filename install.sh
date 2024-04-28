figlet -f slant "Vhost Scanner Installation" | lolcat
sudo apt install figlet lolcat python3 git
python3 -m pip install -r requirements.txt
git clone https://github.com/Shabari-K-S/coloredoutput.git
cd coloredoutput
sudo python3 setup.py install
echo "Installation completed" | lolcat
echo "Run the script by typing python3 vhost_scanner.py" | lolcat 