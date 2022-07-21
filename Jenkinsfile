pipeline {
	agent {
		kubernetes {
			//cloud 'kubernetes'
			yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: maven
    image: maven:3.3.9-jdk-8-alpine
    command: ['cat']
    tty: true
"""
		}
	}
	stages {
		stage('Run maven') {
			steps {
				container('maven') {
					sh 'mvn -version'
					sh 'sleep 300'
             	    sh 'helm install rabbitmq --set auth.username=user,auth.password=Lior12345,auth.erlangCookie=secretcookie,metrics.enabled=true,persistence.enabled=true bitnami/rabbitmq' 
	                sh 'ping -n 45 127.0.0.1 > nul'
		            sh 'kubectl get pods'
		            sh 'echo rabbitmq'	
		            sh 'start /min python ./expose-RabbitMQ.py'	
				}
			}
		}
	}
}
