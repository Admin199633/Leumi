pipeline { 
    agent any
    stages {
        stage('properties') {
            steps {
                git branch: 'main', url: 'https://github.com/Admin199633/Project_Devops.git'
            }
        }
	stage('Creata DND(docker in docker)') {
            steps {
                script {
		    sh 'kubectl apply -f docker.yml'
		    sh 'echo docker in docker'
                }
            }
        }
    }
   
