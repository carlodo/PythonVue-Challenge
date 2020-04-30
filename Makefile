lint:
	docker exec -it moti-reduced_backend_1 pylama
	docker exec -it moti-reduced_frontend_1 npx eslint . --ext .js,.vue
