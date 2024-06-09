pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Araelka/AMO_2.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Download Data') {
            steps {
                sh 'python data_download.py'
            }
        }
        stage('Preprocess Data') {
            steps {
                sh 'python data_preprocessing.py'
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
}