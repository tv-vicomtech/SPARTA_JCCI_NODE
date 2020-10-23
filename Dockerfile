# Use the official image as a parent image.
FROM effezeta88/pep-proxy_rest-api

WORKDIR /home/

ADD flaskserver.py .

WORKDIR /opt/fiware-pep-proxy

# Run the command inside your image filesystem.
RUN sed -i "s|cert/cert.crt|cert/cert.pem|g" /opt/fiware-pep-proxy/config.js
RUN sed -i "s|cert/key.key|cert/privakey.pem|g" /opt/fiware-pep-proxy/config.js
RUN sed -i -e "/privakey.pem/a\\  ca_cert: \['cert/chain.pem', 'cert/fullchain.pem'\]," /opt/fiware-pep-proxy/config.js

ADD init_script.sh .
RUN chmod +x init_script.sh
ENTRYPOINT ["./init_script.sh"]