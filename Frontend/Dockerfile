FROM node:18-alpine as tts-frontend

WORKDIR /app

COPY package.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:1.21.3-alpine as prod
COPY --from=tts-frontend /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80