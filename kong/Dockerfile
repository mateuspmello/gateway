FROM kong:3.6.1
USER 0
RUN mkdir -p /kong/declarative/
COPY kong.yml /kong/declarative/
RUN cp /etc/kong/kong.conf.default /etc/kong/kong.conf

USER root
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y unzip
RUN apt-get install -y luarocks

# RUN luarocks install kong-plugin-jwt-keycloak
# ENV PLUGIN_VERSION=1.3.0-1
# RUN luarocks make
# RUN luarocks pack kong-plugin-jwt-keycloak ${PLUGIN_VERSION}

# RUN luarocks install kong-oidc

# RUN git clone --branch v1.2.5-1 https://github.com/revomatico/kong-oidc.git
# WORKDIR /kong-oidc
# RUN luarocks make

# ENV OIDC_PLUGIN_VERSION=1.2.5-1
# RUN luarocks pack kong-oidc ${OIDC_PLUGIN_VERSION} \
#      && luarocks install kong-oidc-${OIDC_PLUGIN_VERSION}.all.rock

# USER kong

ENV JWT_PLUGIN_VERSION=1.3.0-1
WORKDIR /
# RUN git clone https://github.com/telekom-digioss/kong-plugin-jwt-keycloak

RUN git clone https://github.com/mateuspmello/kong-plugin-jwt-keycloak
WORKDIR /kong-plugin-jwt-keycloak
RUN luarocks make
RUN luarocks pack kong-plugin-jwt-keycloak ${JWT_PLUGIN_VERSION} \
     && luarocks install kong-plugin-jwt-keycloak-${JWT_PLUGIN_VERSION}.all.rock

