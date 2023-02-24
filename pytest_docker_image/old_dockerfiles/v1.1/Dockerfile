FROM benjose22/selenium_pytest_remote:v1.0
LABEL maintainer="Ben Jose" 
LABEL email="benjose22@gmail.com"

WORKDIR /src
RUN mkdir /AllureReports
RUN chmod -R 777 /AllureReports

ENTRYPOINT ["pytest","-p","no:cacheprovider","--alluredir=/AllureReports"]
CMD ["--help"]