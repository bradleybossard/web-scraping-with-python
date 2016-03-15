#FROM ubuntu:15.04
FROM bradleybossard/docker-common-devbox

RUN apt-get update --fix-missing --yes

RUN apt-get install --yes python3 python3-pip vim python3-bs4 jq less

WORKDIR /src

CMD bash
