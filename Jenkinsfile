#!groovy
pipeline {
    agent any

    stages{

      stage('Build'){
        steps {
          sh 'docker-compose -f docker/docker-compose-db.yml up -d'
        }
        post {
            always {
               sh 'docker run --rm -v $JENKINS_JOBS:/var/jenkins_home/jobs --workdir $BUILD_WORKSPACE alpine:latest chown -R $UID:$GID .'
            }
            failure {
               sh 'docker-compose -f docker/docker-compose-prepare-db.yml down'
               deleteDir()
            }
        }
      }

    }
}
