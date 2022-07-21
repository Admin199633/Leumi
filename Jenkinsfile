
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
	stage('Build Docker image - locally') {
            steps {
                script{
                    bat "docker build -t devops_producer:%BUILD_NUMBER% ./producer"
                    bat "docker build -t devops_consumer:%BUILD_NUMBER% ./consumer"
		    bat "start/min docker run -p -p 127.0.0.1:8777:8777 $BUILD_NUMBER"
                }
            }
         }
	stage('docker push') {
            steps {
                script {
                    bat 'docker tag devops_producer:%BUILD_NUMBER% photop/devops_producer:%BUILD_NUMBER%'
                    bat 'docker push photop/devops_producer:%BUILD_NUMBER%'
                    bat 'docker tag devops_consumer:%BUILD_NUMBER% photop/devops_consumer:%BUILD_NUMBER%'
                    bat 'docker push photop/devops_consumer:%BUILD_NUMBER%'
		    bat 'echo docker push'	
                 }
            }
        } 
        stage('Helm create producer') {
            steps {
                script {
	            bat 'helm create poducer'
                    bat 'helm install producer --set image.tag=%BUILD_NUMBER% ./producer-helm '
		    bat 'start python ./producer/producer.py -p 5672 -s localhost -m "Hello Nuni" -r 30'
		    bat 'kubectl get pods'	
                 }
            }
        } 
        stage('Helm create consumer') {
            steps {
                script {
	            bat 'helm create consumer'
                    bat 'helm install consumer --set image.tag=%BUILD_NUMBER% ./consumer-helm '
		    bat 'start  python ./consumer/consumer.py -p 5672 -s localhost'
		    bat 'kubectl get pods'	
                 }
            }
        } 	
	stage('monitoring') {
            steps {
                script {
		    bat 'helm repo update'
		    bat 'kubectl apply -f ./monitoring/namespace.yml '
		    bat 'helm install prometheus --namespace monitoring   prometheus-community/prometheus'	
	            bat 'kubectl apply -f monitoring/config.yml'
		    bat 'helm install -f monitoring/values.yml  --namespace monitoring --set service.port=3000  grafana grafana/grafana'
		    bat 'kubectl get pods -n monitoring'	
		    bat 'ping -n 25 127.0.0.1 > nul'
		    bat 'start python expose-prometheus .py'
		    bat 'start python expose-grafana.py'
		    bat 'ping -n 1000 127.0.0.1 > nul'	
                }
            }
        }
}
