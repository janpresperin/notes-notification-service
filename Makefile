format:
	black .


create-aws-lambda-package:
	rm aws-deployment-package.zip
	rm -r package
	pip install --target ./package requests python-dotenv
	cd package && zip -r ../aws-deployment-package.zip .
	zip aws-deployment-package.zip .env helperutils.py notifier.py lambda_function.py kindle_clippings.csv models.py