pipeline {
	agent {
		kubernetes {
			//cloud 'kubernetes'
			yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: helm
    image: alpine/helm:latest
    command: ['cat']
    tty: true
"""
		}
	}
	stages {
		stage('Run maven') {
			steps {
				container('helm') {
					sh 'helm list'
					sh'apt-get install helm'
					sh'apt-get install minikube'
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
