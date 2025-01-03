pipeline {
    agent any
    environment {
        VENV_DIR = 'myenv'  // Nom du répertoire de l'environnement virtuel
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/boughjihen/Jenkins_projet.git'
            }
        }
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                cd App
                if [ ! -d "$VENV_DIR" ]; then
                    python3 -m venv $VENV_DIR
                fi
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                cd App
                source $VENV_DIR/bin/activate
                pytest tests/
                '''
            }
        }
        stage('Deploy Application') {
            steps {
                echo 'Deploying application...'
                sh '''
                cd App
                source $VENV_DIR/bin/activate
                python3 app.py &
                '''
            }
        }
    }
    post {
        always {
            echo 'Cleaning up workspace...'
            sh '''
            cd App
            if [ -d "$VENV_DIR" ]; then
                rm -rf $VENV_DIR
            fi
            '''
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
