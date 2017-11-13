#!groovy
pipeline {
    agent any

    environment {
        BACKEND_API_CODE = "$WORKSPACE"
    }

    stages{
      stage('Build'){
        steps {
          sh 'docker-compose -f $WORKSPACE/docker-compose-db.yml up -d'
        }
        post {
          failure {
            sh 'docker-compose -f $WORKSPACE/docker-compose-db.yml down'
          }
        }
      }

      stage('Unit Tests'){
        steps{
          sh 'docker-compose -f $WORKSPACE/docker-compose-test.yml up'
        }

        post {
          always {
            sh 'docker-compose -f $WORKSPACE/docker-compose-db.yml down --volume'
          }
          failure {
            sh 'docker-compose -f $WORKSPACE/docker-compose-db.yml down'
          }
        }
      }
    }

    post {
        always {
            sh 'ls -lh $WORKSPACE/myproject/'
            sh 'ls -lh $WORKSPACE/myproject/reports'
            sh 'sudo chown jenkins $WORKSPACE/myproject/reports/coverage.xml'
            sh 'sudo chown jenkins $WORKSPACE/myproject/reports/junit.xml'
            sh 'sudo chgrp jenkins $WORKSPACE/myproject/reports/coverage.xml'
            sh 'sudo chgrp jenkins $WORKSPACE/myproject/reports/junit.xml'
            sh 'ls -lh $WORKSPACE/myproject/reports'
            junit '$WORKSPACE/myproject/reports/junit.xml'
            step([$class: 'CoberturaPublisher', autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: '$WORKSPACE/myproject/reports/coverage.xml', failUnhealthy: false, failUnstable: false, maxNumberOfBuilds: 0, onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false])
        }
    }

}
