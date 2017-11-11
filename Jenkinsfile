#!groovy
pipeline {
    agent any

    stages{

      stage('Build'){
        steps {
          sh 'env'
          sh 'docker-compose -f $WORKSPACE/docker-compose-db.yml up -d'
        }

        post {
          failure {
             sh 'docker-compose -f docker/docker-compose-db.yml down'
             deleteDir()
          }
        }

      }

    }
}
