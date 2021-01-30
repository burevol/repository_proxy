import os
import re
import jenkins

need_start_job = False
current_client_addr = ()
repo_name = ""

re_alias = re.compile(b'alias=\"(.*?)\"')
JENKINS_ID = os.environ['JENKINS_ID']
JENKINS_TOKEN = os.environ['JENKINS_TOKEN']
JENKINS_ADDR = os.environ['JENKINS_ADDR']
JENKINS_JOB = os.environ['JENKINS_JOB']
JENKINS_PROTOCOL = os.environ['JENKINS_PROTOCOL']

def handle_request(client_request, client_addr):
    global need_start_job
    global repo_name
    global current_client_addr
    if client_request.find(b'DevDepot_commitObjects') != -1:
        need_start_job = True
        alias = re_alias.findall(client_request)
        if (len(alias)>0):
            repo_name = alias[0].decode('utf-8')
            current_client_addr = client_addr
            print("Commit to repository %s found"%repo_name)

    return client_request

def handle_response(server_response, client_addr):
    global need_start_job
    global repo_name
    global current_client_addr

    if need_start_job:
        if client_addr == current_client_addr: 
            if server_response.find(b'HTTP/1.1 200 OK') != -1:
                need_start_job = False
                print("Sync repository %s"%repo_name)
                JENKINS_URL = '%s://%s:%s@%s' % (JENKINS_PROTOCOL, JENKINS_ID, JENKINS_TOKEN, JENKINS_ADDR)
                try:
                    Server = jenkins.Jenkins(JENKINS_URL)
                    Server.build_job(JENKINS_JOB, {'extension_name': repo_name,})
                except:
                    print("Job on server Jenkins couldn't be started")
                repo_name = ""  
    return server_response         

