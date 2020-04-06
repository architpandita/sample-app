FROM python:3
# fetching pre build image of python with linux OS from dockerhub,
# you can find more base images in dockerhub like ubuntu, java etc


COPY sample/ /src/sample
# This will copy the "sample" directory to "src" folder of python's Linux docker image
# docker has two cmds: 1) COPY for copying files/folder from local system
#                      2) ADD to copy from other system or local

WORKDIR /src/sample
# Change current directory to "sample" dir, taking us inside "sample" folder

RUN pip install -r requirements.txt
# RUN is use to run any cmd in new creating layer like you run commands in terminal or CMD


# ----  Above this is setup layer of docker which is related to setting up environment
# to perform those actions that you need before running application in Setup layer, these run at "docker build "
# ----  Below write application running commands something like performing task after your windows is boot up
# so this is kind of execution layer it will run on " docker run "


CMD [ "python", "./json_csv.py"]
# CMD is similar to RUN but is use in already created layer of docker
