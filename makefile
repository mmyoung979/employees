DC=docker-compose

run-tests: ## Perform all tests
	@$(DC) exec employees python -m pytest -s