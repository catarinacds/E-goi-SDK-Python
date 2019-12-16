import groovy.json.JsonSlurperClassic

timeout(time: 15, unit: 'MINUTES') {
    node {
       stage('Git SCM') {
           checkout scm
       }
       stage('Build') {
           sh "openapi-generator generate -i https://dev-api.egoiapp.com/openapi -g python -o . -c configPython.json"

           sh "rm -rf target/"
       }
       stage('Deploy') {
           def json = readFile(file:'configPython.json')
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
