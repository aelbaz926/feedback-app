FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html

# Optional: if using /api backend on another service
# Add reverse proxy to Flask backend
COPY nginx.conf /etc/nginx/conf.d/default.conf
