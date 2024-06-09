pipeline {
    agent any
    stages {
        stage('Сбор данных') {
            steps {
                script {
                    // Выполняем Python скрипт для загрузки данных
                    sh 'python3 load_data.py'
                }
            }
        }
        stage('Подготовка данных') {
            steps {
                script {
                    // Выполняем Python скрипт для подготовки данных
                    sh 'python3 prepare_data.py'
                }
            }
        }
        stage('Обучение модели') {
            steps {
                script {
                    // Выполняем Python скрипт для обучения модели
                    sh 'python3 train_model.py'
                }
            }
        }
        stage('Анализ модели') {
            steps {
                script {
                    // Выполняем Python скрипт для анализа модели
                    sh 'python3 evaluate_model.py'
                }
            }
        }
    }
}