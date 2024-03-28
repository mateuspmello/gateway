FROM kong:3.6.1
USER 0
RUN mkdir -p /kong/declarative/
COPY kong.yml /kong/declarative/
RUN cp /etc/kong/kong.conf.default /etc/kong/kong.conf