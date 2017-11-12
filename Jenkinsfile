#!groovy
pipeline {
    agent any

    environment {
        BACKEND_API_CODE = "$WORKSPACE"
    }

    stages{
      stage('Build'){
        steps {
          sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml up -d'
        }
        post {
          failure {
            sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml down'
          }
        }
      }

      stage('Unit Tests'){
        steps{
          sh 'sudo su'
          sh 'export BACKEND_API_CODE = $WORKSPACE'
          sh 'sudo docker-compose -f $WORKSPACE/docker-compose-test.yml run --entrypoint /bin/bash web -c "python /app/myproject/manage.py test"'
        }

        post {
          always {
            sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml down --volume'
          }
          failure {
            sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml down'
          }
        }
      }
    }
}
