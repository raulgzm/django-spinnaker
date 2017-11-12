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
          sh 'docker-compose -f $WORKSPACE/docker-compose-test.yml run --entrypoint /bin/sh web -c "pip install -r /app/requirements/local.txt; python /app/myproject/manage.py jenkins myproject.apps --pythonpath /app/myproject/myproject/ --enable-coverage"'
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
            sh 'ls -lh'
            sh 'ls -lh /app/myproject/reports'
            step([$class: 'JUnitResultArchiver', testResults: '/app/myproject/reports/junit.xml'])
            step([$class: 'CoberturaPublisher', autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: '/app/myproject/reports/coverage.xml', failUnhealthy: false, failUnstable: false, maxNumberOfBuilds: 0, onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false])
            deleteDir()
            sh "docker rmi ${api.id} -f"
        }
    }

}
