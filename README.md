# JobGraph
An analysis of job offers represented by complex networks.

To scrap the data, please type following commands into your CLI:

	docker build --tag <image_name> .
	docker run -d -it --rm -v $(pwd):/app --name <container_name> <image_name>
	docker exec <container_name> dvc repro

