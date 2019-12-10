import groovy.json.JsonSlurperClassic

timeout(time: 15, unit: 'MINUTES') {
    node {
       stage('Git SCM') {
           checkout scm
       }
       stage('Build') {
           sh 'rm README.md'
           sh "openapi-generator generate -i https://dev-api.egoiapp.com/openapi -g java -o . -c config.json"

           sh "rm -rf target/"
           sh "mvn clean install"
       }
       stage('Test') {
           //add junit tests
       }
       stage('Deploy') {
           def json = readFile(file:'config.json')
           def data = new JsonSlurperClassic().parseText(json)
           def version = data.artifactVersion

           sh "git commit -am \"Version:  ${version}\""
           sh 'git push'
           sh "git tag ${version}"
           sh 'git push --tags'
       }
       stage('SonarQube analysis') {
           withSonarQubeEnv('E-Goi SonarQube') {
             sh "/usr/bin/sonar-scanner"
           }
       }
   }
}