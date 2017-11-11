#!groovy
pipeline {
    agent any

    stages{

      stage('Build'){
        steps {
          sh 'env'
          sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml up -d'
          sh 'sudo docker-compose -f $WORKSPACE/docker-compose-local.yml up -d'
        }

        post {
          failure {
             sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml down'
             sh 'sudo docker-compose -f $WORKSPACE/docker-compose-local.yml down'
             deleteDir()
          }
        }
      }

      stage('Unit Tests'){
        steps{
          sh 'sudo docker-compose -f $WORKSPACE/docker-compose-local.yml run --entrypoint /bin/sh api -c "pip install -r /requirements/local.txt;"'
        }

        post {
          always {
            sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml down --volume'
            sh 'sudo docker-compose -f $WORKSPACE/docker-compose-local.yml down --volume'
          }
          failure {
             sh 'sudo docker-compose -f $WORKSPACE/docker-compose-db.yml down'
             sh 'sudo docker-compose -f $WORKSPACE/docker-compose-local.yml down'
             deleteDir()
          }
        }
      }

    }
}
