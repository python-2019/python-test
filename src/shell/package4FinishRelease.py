import os

from src.util.fileUtil import fileUtil

master = 'master'
develop = 'develop'
username = 'shanmu2020'
password = 'Spring2018418'
release_start = 'mvn jgitflow:release-start -DallowSnapshots=true -DautoVersionSubmodules=true -Dmaven.test.skip=true'
release_finish = 'mvn jgitflow:release-finish -DallowSnapshots=true -Dmaven.test.skip=true -Dmaven.javadoc.skip=true'
pull_push_develop_master_type = '3'
get_file_list_type = '4'

project_parent = 'C:\AA--tima\code\\tima\jmc-b-tsp-sp\codeProject\\'

project_list = {
    project_parent + 'jgitflow-test': 'release-0.0.4',
    project_parent + 'tdata-sync': 'release/0.0.57',
}


def get_current_path():
    """
    获取当前地址
    """
    return os.path.split(os.path.realpath(__file__))[0]


def release_finish_pull_push():
    checkout_master = "git checkout " + master
    print(checkout_master)
    os.system(checkout_master)

    pull_master = "git pull " + master
    print(pull_master)
    os.system(pull_master)

    push_master = "git push " + master
    print(push_master)
    os.system(push_master)

    checkout_develop = "git checkout " + develop
    print(checkout_develop)
    os.system(checkout_develop)

    pull_develop = "git pull " + develop
    print(pull_develop)
    os.system(pull_develop)

    push_develop = "git push " + develop
    print(push_develop)
    os.system(push_develop)


def release_start_pull_push():
    checkout_master = "git checkout " + master
    print(checkout_master)
    os.system(checkout_master)

    pull_master = "git pull " + master
    print(pull_master)
    os.system(pull_master)

    checkout_develop = "git checkout " + develop
    print(checkout_develop)
    os.system(checkout_develop)

    pull_develop = "git pull " + develop
    print(pull_develop)
    os.system(pull_develop)


if __name__ == '__main__':
    print(project_list)
    op = input("请输入你的执行操作:\n1: release_start;\n2:release_finish;\n3:pull push develop,master;\n4:get file list")
    if op == '1':
        op = release_start
    elif op == '2':
        op = release_finish
    elif op == pull_push_develop_master_type:
        pass
    elif op == get_file_list_type:
        dir = input("输入文件夹获取文件列表:")
        print(fileUtil.get_file_list(dir))
        os._exit(0)
    else:
        print("不支持的操作: ", op)
        os._exit(0)

    for dir in project_list.keys():
        print(dir, "开始执行: ", op)
        if os.path.exists(dir) is False:
            print(" 文件不存在", dir)
            continue
        os.chdir(dir)
        if op==release_start:
            release_start_pull_push()
        elif op == '3':
            continue
        elif op == release_finish:
            release_finish_pull_push()
            checkout_release = "git checkout " + project_list[dir]
            print(checkout_release)
            os.system(checkout_release)
        print(op)
        os.system(op)
        print("操作完成: ", dir)
