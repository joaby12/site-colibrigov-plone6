ARG PLONE_VERSION=6.0.0a6
FROM plone/plone-backend:${PLONE_VERSION}

LABEL maintainer="Joaby Souto <joaby@colibrigov.com>" \
      org.label-schema.name="site_plone6-backend" \
      org.label-schema.description="site_plone6 backend image." \
      org.label-schema.vendor="Joaby Souto"

# Add local code
COPY . .

# Install local requirements and fix permissions
RUN ./bin/pip install -r requirements.txt \
    && chown -R plone: /app
