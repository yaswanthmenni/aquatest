pipeline {
   agent {
     node{
       label 'bitcoin'
     }
   }
   stages {
    stage('Checkout') {
      steps {
          checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/yaswanthmenni/aquatest.git']]])
          }
       }
    stage('Build Image'){
      steps{
        sh "docker build --tag yaswanthm/aquatest:latest ."
      }
    }
    stage('Publish Image'){
      steps{
        withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]){
        sh "docker login -u $USERNAME -p $PASSWORD"
        sh "docker push yaswanthm/aquatest:latest"
      }}
    }
  }
}