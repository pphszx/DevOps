# DevOps

```bash
# 创建镜像
$ docker build -t flask_app:v1 .
$ docker image ls -a
$ docker image inspect flask_app:v1

# 推送至Docker Hub
$ docker login
$ docker image tag flask_app:v1 pphszx/flask_app:v1
$ docker push pphszx/flask_app:v1

# 映射本地目录，修改环境变量，方便开发
$ docker container run -p 4000:80 -v $(pwd):/data --name flask_test -e SUPERSET_ENV=dev -d flask_app:v1
$ curl http://0.0.0.0:4000
```
