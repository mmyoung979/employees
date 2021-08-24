FROM node:14.3.0-alpine as build

WORKDIR /usr/src

COPY . .

RUN npm install --silent
RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "start"]
