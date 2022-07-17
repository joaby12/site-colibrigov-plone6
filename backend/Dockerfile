ARG PLONE_VERSION=6.0.0a6
FROM plone/plone-backend:${PLONE_VERSION}

LABEL maintainer="colibrigov <joaby@colibrigov.com>" \
      org.label-schema.name="plone-site-backend" \
      org.label-schema.description="Plone Site backend image." \
      org.label-schema.vendor="colibrigov"

# Add local code
COPY . .

# Install local requirements and fix permissions
RUN ./bin/pip install -r requirements.txt \
    && chown -R plone: /app
