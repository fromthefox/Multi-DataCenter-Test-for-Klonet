import requests

def upload_file_to_container(ip, port, user, topo, node_name, file_path, destination_path):
    """
    从Server发送到Node
    """
    url = f"http://{ip}:{port}/file/uload/"
    payload = {
        "user": user,
        "topo": topo,
        "ne_name": node_name,
        "file_path": destination_path
    }
    with open(file_path, "rb") as f:
        file = {"file": f}
        resp = requests.post(url=url, data=payload, files=file)
        print(f"Response status code for {node_name}: {resp.status_code}")

upload_file_to_container("192.168.1.46", 25890, "yhbian", "Multi_DataCenter_Experiment", "h4", "./worker_node_script_4.py", "/as_exec_file/")