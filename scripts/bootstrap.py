# !/usr/bin/python
import os


def get_username():
    print "Enter bahmni username  - "
    username = raw_input()
    return username


def get_implementation_name():
    print "\nEnter implementation name - "
    implementation_name = raw_input()
    return implementation_name


def execute_command(command):
    os.system(command)


def install_package(package_name):
    installation_command = "sudo yum install -y " + package_name
    execute_command(installation_command)


def clone_package(repo_url):
    clone_command = "git clone " + repo_url
    execute_command(clone_command)


def change_directory(destination):
    os.chdir(destination)


def export_environment_variables(home_directory, environment_variable_name, environment_variable_value):
    bashrc_path = home_directory + "/.bashrc"
    with open(bashrc_path, "a") as bashrc:
        bashrc.write("export " + environment_variable_name + "=" + environment_variable_value)
        bashrc.write("\n")
        bashrc.close()
    return


def add_yum_repo(repo_name, repo_url):
    repo_name = "[" + repo_name + "]\n"
    name = "name=" + repo_name + "\n"
    baseurl = "baseurl=" + repo_url + "\n"
    extras = "enabled=1\ngpgcheck=0"
    file_handle = open("/etc/yum.repos.d/" + repo_name + ".repo", "w")
    file_handle.truncate()
    file_handle.write(repo_name + name + baseurl + extras)
    file_handle.close()
    return

def controller():
    username = get_username()
    implementation_name = get_implementation_name()
    export_environment_variables("/root", "BAHMNI_USER_NAME", username)
    export_environment_variables("/home/" + username, "BAHMNI_USER_NAME", username)
    export_environment_variables("/root", "IMPLEMENTATION_NAME", implementation_name)
    export_environment_variables("/home/" + username, "IMPLEMENTATION_NAME", implementation_name)
    change_directory("/root")
    install_package("git")
    add_yum_repo("tw-bahmni", "http://172.18.2.14/localrepo")
    install_package("wget")
    install_package("ruby")
    install_package("puppet")
    clone_package("https://github.com/bhamni/bahmni-environment")

controller()