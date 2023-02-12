IMAGE_TAG := latest

release: build install-prod

build:
	docker build -t vanderkooi11/glia-app:$(IMAGE_TAG) .
	docker save vanderkooi11/glia-app:$(IMAGE_TAG) > image.tar
	@eval $$(minikube docker-env) ;\
	docker load -i image.tar
	rm image.tar

install-prod:
	helm install glia-app ./helm --values ./helm/vars/production/values.yaml

install-dev:
	helm install glia-app ./helm --values ./helm/vars/production/values.yaml

uninstall:
	helm uninstall glia-app
