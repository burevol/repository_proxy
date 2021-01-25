import os
import re
import jenkins
import json

need_start_job = False
repo_name = ""

re_alias = re.compile(b'alias=\"(.*?)\"')
JENKINS_ID = os.environ['JENKINS_ID']
JENKINS_TOKEN = os.environ['JENKINS_TOKEN']
JENKINS_ADDR = os.environ['JENKINS_ADDR']
JENKINS_JOB = os.environ['JENKINS_JOB']
JENKINS_PROTOCOL = os.environ['JENKINS_PROTOCOL']

def handle_request(client_request):
    global need_start_job
    global repo_name
    if re.search(b'DevDepot_commitObjects', client_request):
        need_start_job = True
        alias = re_alias.findall(client_request)
        if (len(alias)>0):
            repo_name = alias[0].decode('utf-8')

    return client_request

def handle_response(server_response):
    global need_start_job
    global repo_name

    if need_start_job:
        if re.search(b'HTTP/1.1 200 OK', server_response):
            need_start_job = False
            print("Синхронизируем хранилище %s"%repo_name)
            JENKINS_URL = '%s://%s:%s@%s' % (JENKINS_PROTOCOL, JENKINS_ID, JENKINS_TOKEN, JENKINS_ADDR)
            try:
                Server = jenkins.Jenkins(JENKINS_URL)
                Server.build_job(JENKINS_JOB, {'extension_name': repo_name,})
            except:
                print("Не удалось запустить задание на сервере Jenkins")
            repo_name = ""  
    return server_response         

