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
            sh 'rm -r /myproject/'
          }
        }
      }

      stage('Unit Test'){
      steps {
          sh 'env'
          sh '/myproject/bin/activate'
          sh 'cd /webapps/django-docker/myproject/'
          sh 'pip install -r ../requirements/local.txt'
          sh 'python manage.py migrate'
          sh 'python manage.py test'
        }
        post {
          always {
            sh 'rm -r /myproject/'
          }
        }
      }

    }
}
