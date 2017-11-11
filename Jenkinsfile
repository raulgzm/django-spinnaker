#!groovy
pipeline {
    agent any

    environment {
        BACKEND_API_CODE = "$WORKSPACE"
    }

    stages{
      stage('Build'){
        steps {
          sh 'env'
          sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml up -d'
          sh 'sudo docker-compose -f $WORKSPACE/docker-compose-test.yml up -d'
        }

        post {
          failure {
             //sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml down'
             //sh 'sudo docker-compose -f $WORKSPACE/docker-compose-test.yml down'
             deleteDir()
          }
        }
      }

      stage('Unit Tests'){
        steps{
          sh 'sudo docker-compose -f $WORKSPACE/docker-compose-test.yml run --entrypoint /bin/sh "python manage.py test"'
        }

        post {
          always {
            //sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml down --volume'
            //sh 'sudo docker-compose -f $WORKSPACE/docker-compose-test.yml down --volume'
          }
          failure {
             //sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml down'
             //sh 'sudo docker-compose -f $WORKSPACE/docker-compose-local.yml down'
             deleteDir()
          }
        }
      }

    }
}
