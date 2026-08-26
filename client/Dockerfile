# Build stage
FROM node:26-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Serve stage
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
# If using Create React App instead of Vite, use /app/build above instead of /app/dist
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
