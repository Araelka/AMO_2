pipeline {
    agent any
    stages {
        stage('Сбор данных') {
            steps {
                script {
                    // Выполняем Python скрипт для загрузки данных
                    sh 'python load_data.py'
                }
            }
        }
        stage('Подготовка данных') {
            steps {
                script {
                    // Выполняем Python скрипт для подготовки данных
                    sh 'python prepare_data.py'
                }
            }
        }
        stage('Обучение модели') {
            steps {
                script {
                    // Выполняем Python скрипт для обучения модели
                    sh 'python train_model.py'
                }
            }
        }
        stage('Анализ модели') {
            steps {
                script {
                    // Выполняем Python скрипт для анализа модели
                    sh 'python evaluate_model.py'
                }
            }
        }
    }
}