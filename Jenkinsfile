#!groovy
pipeline {
    agent any

    stages{

      stage('Build'){
        steps {
          sh 'env'
          sh 'pip install -r $WORKSPACE/requirements/local.txt'
        }
      }

      stage('Unit Test'){
      steps {
          sh 'python $WORKSPACE/myproject/manage.py migrate'
          sh 'python $WORKSPACE/myproject/manage.py test'
        }
      }

    }
}
