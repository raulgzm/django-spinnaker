#!groovy

import groovy.json.JsonOutput

def notifyMonitor(buildStatus, endpoint, buildPhase="FINALIZED") {

    def payload = JsonOutput.toJson([
        name: env.JOB_NAME,
        duration: currentBuild.duration,
        build      : [
            number: env.BUILD_NUMBER,
            phase: buildPhase,
            status: buildStatus,
            full_url: env.BUILD_URL,
        ]
    ])

    sh "curl --silent -X POST -H 'Content-Type: application/json' -d '${payload}' ${endpoint}"
}

pipeline {
    agent any

    environment {
        BACKEND_API_CODE = "$WORKSPACE"
        MONITOR_URL = 'http://192.168.33.56/projects/85ef55a4-fc3a-4c4b-a48e-7f2a50f665b0/status'
    }

    stages{
      stage('Build'){
        steps {
          sh 'docker-compose -f $WORKSPACE/docker-compose-db.yml up -d'
          if(env.BRANCH_NAME == 'master'){
            MONITOR_URL = 'http://192.168.33.56/projects/a99955b5-aad2-4a5a-9260-5245952c4103/status'
          }
          else {
            MONITOR_URL = 'http://192.168.33.56/projects/85ef55a4-fc3a-4c4b-a48e-7f2a50f665b0/status'
          }
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
            step([$class: 'JUnitResultArchiver', testResults: 'myproject/reports/junit.xml'])
            step([$class: 'CoberturaPublisher', autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'myproject/reports/coverage.xml', failUnhealthy: false, failUnstable: false, maxNumberOfBuilds: 0, onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false])
        }

        success {
            notifyMonitor("SUCCESS", $MONITOR_URL)
        }

        unstable {
            notifyMonitor("UNSTABLE", $MONITOR_URL)
        }

        failure {
            notifyMonitor("FAILURE", $MONITOR_URL)
        }
    }

}
