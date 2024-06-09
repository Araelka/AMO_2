pipeline {
    agent any

    stages {
        stage('Download Data') {
            steps {
                sh 'wget https://github.com/gainadir12/Diabet/archive/refs/heads/main.zip -O diabet_data.zip'
                sh 'unzip diabet_data.zip'
            }
        }
        stage('Process Data') {
            steps {
                sh 'source ml_env/bin/activate && python process_data.py'
            }
        }
        stage('Train Model') {
            steps {
                sh 'source ml_env/bin/activate && python train_model.py'
            }
        }
        stage('Evaluate Model') {
            steps {
                sh 'source ml_env/bin/activate && python evaluate_model.py'
            }
        }
    }
}