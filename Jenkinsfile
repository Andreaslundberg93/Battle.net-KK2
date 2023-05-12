pipeline {
    agent { label "built-in" }
    stages {
        stage("Running tests") {
            steps { 
                dir('C:/Users/aandr/Documents/GitHub/Battle.net-KK2/test_inet')
                bat "python -m unittest" 
                echo "Testing" 
            }
                 
        } 
    } 
    post("Cleanup") {
        always { 
            cleanWs() 
            echo "Cleaning up" 
            } 
        } 
    }