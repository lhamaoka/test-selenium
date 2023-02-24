# Create a selenium pytest image without any browsers and browser drivers
FROM ubuntu
MAINTAINER Ben Jose <benjose22@gmail.com>
RUN mkdir /src
RUN apt-get update
RUN apt-get update && apt-get install -y \
    python3.7 \
    python3-pip
RUN pip3 install selenium \
	pytest-xdist \
	allure-pytest

WORKDIR /src
ENTRYPOINT ["pytest","-p","no:cacheprovider"]
CMD ["--help"]
