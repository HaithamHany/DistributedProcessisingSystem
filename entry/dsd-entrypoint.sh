echo "Installing unzip" >&2
apt-get install unzip
echo "Unzipping the dataset" >&2
unzip /home/shared/dataset.zip
tail -f /dev/null