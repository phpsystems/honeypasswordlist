#!/usr/bin/env bash
set -euo pipefail

# Setup SSH Keys for the tsec user for this to work. 
# Also, set up the git repo before hand as well. Both with SSH keys, for the win :-)

ssh -p 64295 tsec@tpot -C "python3 /opt/honeypasswordlist/elastic2passwordlist.py" > /root/passwordlist/pass.tmp
cd /root/passwordlist/
mv passwordcombo.list{,.old}
cat passwordcombo.list.old pass.tmp | sort | uniq > passwordcombo.list
git add passwordcombo.list
git commit -m "Daily auto commit"
git push origin master
