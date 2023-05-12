pipeline {
    agent any
    stages {
        stage("Running tests") {
            steps { 
                
                bat "python -m unittest test_inet.py" 
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