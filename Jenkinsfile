#!groovy
pipeline {
    agent any

    environment {
        BUILD_WORKSPACE = "${env.WORKSPACE.replace(env.JENKINS_JOBS, '/var/jenkins_home/jobs')}"
    }

    stages{

      stage('Build'){
        steps {
          sh virtualenv -p /usr/bin/python3.4 myproject
          source /myproject/bin/activate
          cd /webapps/django-docker/myproject/
          pip install -r ../requirements/local.txt
          python manage.py migrate
          python manage.py test
        }
        post {
          always {
            sh rm -r /myproject/
          }
          failure {
            sh rm -r /myproject/
          }
        }
      }

    }
}
