from flask import Flask, render_template, jsonify, request, redirect, url_for
import docker

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/build_docker_img', methods=['GET'])
# @jwt_required
def build_docker_image():
    try:
        client = docker.from_env()
        print(client.images)
        new_image = client.images.build(path="/docker_template", tag='chatbot',
                                        dockerfile='/docker_template/Dockerfile')

        # ret = subprocess.run(['docker', 'save', '-o', './chatbot2.tar', 'chatbot'])
        # print(ret)
        username = "admin sure"
        return jsonify({'hello': 'from {}'.format(username)}), 200
    except Exception as ex:
        print(ex)
        return jsonify({'hello': str(ex)}), 200


if __name__ == '__main__':
    app.run()
