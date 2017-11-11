#!groovy
pipeline {
    agent any

    stages{

      stage('Build'){
        steps {
          sh 'virtualenv -p /usr/bin/python3.4 myproject'
        }
        post {
          failure {
            sh 'rm -r $WORKSPACE/myproject/'
          }
        }
      }

      stage('Unit Test'){
      steps {
          sh 'env'
          sh '$WORKSPACE/myproject/bin/activate'
          sh 'pip install -r $WORKSPACE/requirements/local.txt'
          sh 'python $WORKSPACE/myproject/manage.py migrate'
          sh 'python $WORKSPACE/myproject/manage.py test'
        }
        post {
          always {
            sh 'rm -r $WORKSPACE/myproject/'
          }
        }
      }

    }
}
