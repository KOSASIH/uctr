stages:
  - build
  - deploy

build:
  stage: build
  script:
    - docker build -t my-app .
    - docker push my-app:latest

deploy:
  stage: deploy
  script:
    - kubectl apply -f deployment.yaml
    - kubectl rollout status deployment/my-app
