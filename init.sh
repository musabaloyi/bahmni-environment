# Make sure the box file is in the folder
cp setup/vagrant* ~/.ssh/
vagrant up
ssh -t root@$1 'cp -r /home/vagrant/.ssh .'

# yum -y install yum-utils.noarch
# yumdownloader --resolve 