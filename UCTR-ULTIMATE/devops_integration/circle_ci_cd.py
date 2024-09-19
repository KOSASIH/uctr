version: 2.1

orbs:
  node: circleci/node@4.2.0

jobs:
  build-and-deploy:
    executor: node
    steps:
      - checkout
      - run: npm install
      - run: npm run build
      - run: docker build -t my-app .
      - run: docker push my-app:latest
      - deploy:
          name: Deploy to Kubernetes
          command: kubectl apply -f deployment.yaml
