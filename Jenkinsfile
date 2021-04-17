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
        sh "docker push yaswanthm/aquatest:latest"
      }
    }
    }
}