#!groovy
pipeline {
    agent any

    stages{

      stage('Build'){
        steps {
          sh 'env'
          sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml up -d'
        }

        post {
          failure {
             sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml down'
             deleteDir()
          }
        }

      }

    }
}
