pipeline {
    agent any
    stages {
        stage('Копирование репрозитория') {
            steps {
                git branch: 'main', url: 'https://github.com/Araelka/AMO_2.git'
            }
        }
        stage('Установка библиотек') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Сбор данных') {
           steps {
                script {
                    // Выполняем Python скрипт для загрузки данных
                    bat 'python download_data.py'
                }
             }
         }
        stage('Подготовка данных') {
             steps {
                script {
                     // Выполняем Python скрипт для подготовки данных
                     bat 'python process_data.py'
                 }
             }
         }
         stage('Обучение модели') {
             steps {
                script {
                    // Выполняем Python скрипт для обучения модели
                    bat 'python train_model.py'
                 }
             }
        }
         stage('Анализ модели') {
            steps {
                script {
                     // Выполняем Python скрипт для анализа модели
                     bat 'python evaluate_model.py'
                 }
             }
         }
    }
}