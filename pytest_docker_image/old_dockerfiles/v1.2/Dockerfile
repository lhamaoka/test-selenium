FROM benjose22/selenium_pytest_remote:v1.1
LABEL maintainer="Ben Jose" 
LABEL email="benjose22@gmail.com"
WORKDIR /entrypoint
COPY ./entrypoint.sh /entrypoint
RUN chmod +x /entrypoint/entrypoint.sh
WORKDIR /src
ENTRYPOINT ["/entrypoint/entrypoint.sh"]
CMD ["--help"]