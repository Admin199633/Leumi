
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
				}
			}

	stage('rabbitmq') {
            steps {
                script {
	            bat 'helm install rabbitmq --set auth.username=user,auth.password=Lior12345,auth.erlangCookie=secretcookie,metrics.enabled=true,persistence.enabled=true bitnami/rabbitmq' 
	            bat 'ping -n 45 127.0.0.1 > nul'
		    bat 'kubectl get pods'
		    bat 'echo rabbitmq'	
		    bat 'start /min python ./expose-RabbitMQ.py'	
                 }
            }
        }
