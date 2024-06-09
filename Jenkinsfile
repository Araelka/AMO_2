pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Araelka/AMO_2/'
            }
        }
        }
        stage('Download Data') {
            steps {
                sh 'python download_data.py'
            }
        }
        stage('Preprocess Data') {
            steps {
                sh 'python process_data.py'
            }
        }
        stage('Train Model') {
            steps {
                sh 'python train_model.py'
            }
        }
        stage('Evaluate Model') {
            steps {
                sh 'python evaluate_model.py'
            }
        }
    }