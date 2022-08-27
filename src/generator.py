#!/usr/bin/env python3

# Import the os module
from os import chdir, getcwd
from os.path import abspath, dirname

# change to directory above the script (root of this repository)
chdir(dirname(dirname(abspath(__file__))))

nginx_conf_filename = getcwd() + "/referral-spam.conf"

nginx_conf_contents = """# https://github.com/dvershinin/referrer-spam-blocker
# Updated 2022-08-23 13:00:22
#
# /etc/nginx/conf.d/referral-spam.conf
#
# Drop referral-spam.conf to an included directory, e.g. in /etc/nginx/conf.d, or include it manually:
#
#     include referral-spam.conf;
#
# Add the following to each /etc/nginx/site-available/your-site.conf that needs protection:
#
#      server {
#        if ($bad_referer) {
#          return 444;
#        }
#      }
#

map $http_referer $http_referer_host {
    "~^(?:https?://)?([^/]+)" $1;
}

map $http_referer_host $bad_referer {
    hostnames;
    default 0;
"""

with open('src/domains.txt', 'r') as f:
    domains = f.readlines()
    for domain in domains:
        nginx_conf_contents += f"\n    .{domain.strip()} 1;"
nginx_conf_contents += "\n}\n"
print(nginx_conf_contents)

with open(nginx_conf_filename, "w") as f:
    f.write(nginx_conf_contents)