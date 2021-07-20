## Bulletin

# Deployment

### Compiles and hot-reloads for development
in the directory of "frontend/installing-tailwindcss-with-vue-cli"
```
yarn serve
```
to run the front end.

And then make a container
```
docker run -it -p 8001:8001 -v `pwd`:/code --name guestbook python:39
```

Excute the container
```
docker exec -it guestbook /bin/bash
```

then in the directory of "backend/api"

```
./manage.py runserver 0.0.0.0:8001
```

then it should work.

Basically I set my django environment into the docker, which is the instance of "python39" docker image. And Vue's dependencies are in my local PC. So your local environment should support Vue2... and Tailwind maybe.. or the CSS may probabaly cannot work.



# Display



![Display](/frontend/installing-tailwindcss-with-vue-cli/src/img/display.png)
