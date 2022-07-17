pipeline { 
    agent any
    environment { 
        registry = "photop/micro_focus" 
        registryCredential = 'dockerhub_id'
        dockerImage = ""
    } 
    stages {
        stage('properties') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                    properties([buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20')),])
                }
		git branch: 'main', url: 'https://github.com/Admin199633/Main.git'
            }
        }
        stage('Build:Flask.py') {
            steps {
                script {
                    bat 'start python selenium.py'
                    bat 'echo success selenium.py'
                }
            }
        }
