# nginx/Dockerfile

FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY devops/nginx/nginx.conf /etc/nginx/conf.d
# COPY devops/nginx/front.conf /etc/nginx/conf.d
# COPY devops/nginx/built.conf /etc/nginx/conf.d

EXPOSE 80